import httplib2
import argpare
import base64
import os
import re
import subprocess
import sys
import textwrap
import textwrap
import urllib.parse
import xml.etree.ElementTree as etree

class CalcurseCalDAV {

    def __init__(self):

        # Initialize the XML namespace map.
        self.nsmap = {"D": "DAV:", "C": "urn:ietf:params:xml:ns:caldav"}

        # Initialize default values.
        self.configfn = os.path.expanduser("~/.calcurse/caldav/config")
        self.lockfn = os.path.expanduser("~/.calcurse/caldav/lock")
        self.syncdbfn = os.path.expanduser("~/.calcurse/caldav/sync.db")
        self.hookdir = os.path.expanduser("~/.calcurse/caldav/hooks/")
        self.oauth_file = os.path.expanduser("~/.calcurse/caldav/oauth2_cred")
        self.parse_args()
        self.read_config()


    def parse_args(self):
        # Parse command line arguments.
        parser = argparse.ArgumentParser('calcurse-caldav')
        parser.add_argument('--init', action='store', dest='init', default=None,
                            choices=['keep-remote', 'keep-local', 'two-way'],
                            help='initialize the sync database')
        parser.add_argument('--config', action='store', dest='configfn',
                            default=configfn,
                            help='path to the calcurse-caldav configuration')
        parser.add_argument('--lockfile', action='store', dest='lockfn',
                            default=lockfn,
                            help='path to the calcurse-caldav lock file')
        parser.add_argument('--syncdb', action='store', dest='syncdbfn',
                            default=syncdbfn,
                            help='path to the calcurse-caldav sync DB')
        parser.add_argument('--hookdir', action='store', dest='hookdir',
                            default=hookdir,
                            help='path to the calcurse-caldav hooks directory')
        parser.add_argument('--password', action='store', dest='password',
                            default=None,
                            help='password for basic authentication')
        parser.add_argument('--authcode', action='store', dest='authcode',
                            default=None,
                            help='auth code for OAuth2 authentication')
        parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                            default=False,
                            help='print status messages to stdout')
        parser.add_argument('--debug', action='store_true', dest='debug',
                            default=False, help='print debug messages to stdout')
        args = parser.parse_args()

        self.init = args.init is not None
        self.configfn = args.configfn
        self.lockfn = args.lockfn
        self.syncdbfn = args.syncdbfn
        self.hookdir = args.hookdir
        self.password = args.password
        self.authcode = args.authcode
        self.verbose = args.verbose
        self.debug = args.debug


    def read_config(self):
        # Read configuration.
        config = configparser.RawConfigParser()
        if verbose:
            print('Loading configuration from ' + configfn + '...')
        try:
            config.readfp(open(configfn))
        except FileNotFoundError as e:
            die('Configuration file not found: {}'.format(configfn))

        hostname = config.get('General', 'HostName')
        path = '/' + config.get('General', 'Path').strip('/') + '/'
        hostname_uri = 'https://' + hostname
        absolute_uri = hostname_uri + path

        if config.has_option('General', 'InsecureSSL'):
            insecure_ssl = config.getboolean('General', 'InsecureSSL')
        else:
            insecure_ssl = False

        if config.has_option('General', 'Binary'):
            calcurse = config.get('General', 'Binary')
        else:
            calcurse = 'calcurse'

        if config.has_option('General', 'DryRun'):
            dry_run = config.getboolean('General', 'DryRun')
        else:
            dry_run = True

        if not verbose and config.has_option('General', 'Verbose'):
            verbose = config.getboolean('General', 'Verbose')

        if not debug and config.has_option('General', 'Debug'):
            debug = config.getboolean('General', 'Debug')

        if config.has_option('General', 'AuthMethod'):
            authmethod = config.get('General', 'AuthMethod').lower()
        else:
            authmethod = 'basic'

        if config.has_option('Auth', 'UserName'):
            username = config.get('Auth', 'UserName')
        else:
            username = None

        if config.has_option('Auth', 'Password') and not password:
            password = config.get('Auth', 'Password')

        if config.has_section('CustomHeaders'):
            custom_headers = dict(config.items('CustomHeaders'))
        else:
            custom_headers = {}

        if config.has_option('OAuth2', 'ClientID'):
            client_id = config.get('OAuth2', 'ClientID')
        else:
            client_id = None

        if config.has_option('OAuth2', 'ClientSecret'):
            client_secret = config.get('OAuth2', 'ClientSecret')
        else:
            client_secret = None

        if config.has_option('OAuth2', 'Scope'):
           scope = config.get('OAuth2', 'Scope')
        else:
           scope = None

        if config.has_option('OAuth2', 'RedirectURI'):
            redirect_uri = config.get('OAuth2', 'RedirectURI')
        else:
            redirect_uri = 'http://127.0.0.1'

        # Show disclaimer when performing a dry run.
        if dry_run:
            warn(('Dry run; nothing is imported/exported. Add "DryRun = No" to the '
                  '[General] section in the configuration file to enable '
                  'synchronization.'))

        # Check whether the specified calcurse binary is executable and compatible.
        ver = calcurse_version()
        if ver is None:
            die('Invalid calcurse binary. Make sure that the file specified in ' +
                'the configuration is a valid and up-to-date calcurse binary.')
        elif ver < (4, 0, 0, 96):
            die('Incompatible calcurse binary detected. Version >=4.1.0 is required ' +
                'to synchronize with CalDAV servers.')
