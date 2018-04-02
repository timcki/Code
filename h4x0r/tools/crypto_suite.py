import frequency_analzyer
from subprocess import call
from termcolor import colored

class MainMenu:

    def __init__(self):
        self.used_module = 'analyzer'
        self.welcome_message = 'ft3\'s crypto suite'

        self.prompt_symbols =   {
            'main_prompt':          ' [~] ',
            'analyzer_prompt':      colored(' [A] ', 'cyan')
        }

        call(['figlet', self.welcome_message])
        self.prompt = '<' + self.prompt_symbols['main_prompt'] + '> '
        
    def print_prompt(self):
       choice = input(self.prompt)
       return choice

    def loop(self):
        ch = self.print_prompt() 
        fa = frequency_analzyer.FrequencyAnalyzer()
        fa.analyze(ch)



menu = MainMenu()
menu.loop()
