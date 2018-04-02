# This file should be generated by the ./configure script
CC=gcc
WITH_GPL=1
# HOST_CC=@HOST_CC@

DESTDIR=
PREFIX=/usr
BINDIR=/usr/bin
LIBDIR=/usr/lib
MANDIR=/usr/share/man
DOCDIR=/usr/share/doc/radare2
DATADIR=/usr/share
INCLUDEDIR=/usr/include

HAVE_LIB_GMP=0
USE_RPATH=0
HAVE_JEMALLOC=1
HAVE_FORK=1

MKPLUGINS=mk/stat.mk mk/sloc.mk

COMPILER=gcc
STATIC_DEBUG=0
RUNTIME_DEBUG=1
DEBUGGER=1

INSTALL_DIR=/usr/bin/install -d
INSTALL_DATA=/usr/bin/install -m 644
INSTALL_PROGRAM=/usr/bin/install -m 755
INSTALL_SCRIPT=/usr/bin/install -m 755
INSTALL_MAN=/usr/bin/install -m 444
INSTALL_LIB=/usr/bin/install -m 755 -c

VERSION=2.3.0-git
LIBVERSION=2.3.0-git

# ./configure --with-ostype=[linux,osx,solaris,windows] # TODO: rename to w32, w64?
OSTYPE=gnulinux
BUILD_OS=linux
HOST_OS=linux
# hack: must be fixed in acr
ifneq ($(OSTYPE),darwin)
DL_LIBS=-ldl
endif
ifeq ($(OSTYPE),qnx)
DL_LIBS=
endif
WITHPIC=1
WITHNONPIC=0

# capstone
USE_CAPSTONE=0
ifeq ($(USE_CAPSTONE),1)
CAPSTONE_CFLAGS=
CAPSTONE_LDFLAGS=
else
CAPSTONE_CFLAGS=
CAPSTONE_LDFLAGS=
endif

HAVE_LIB_GMP=0
HAVE_LIB_SSL=0
HAVE_LIB_MAGIC=0
USE_LIB_MAGIC=0
USE_LIB_ZIP=0
LIBMAGIC=-lr_magic
LIBZIP=-lrz

SSL_CFLAGS=
SSL_LDFLAGS=

GIT_TIP:=$(shell (git rev-parse HEAD 2>/dev/null || echo HEAD ))
GIT_TAP:=$(shell (git describe --tags 2>/dev/null || echo ${VERSION} ))

# cache compiler flags at configure time #
CFLAGS+=
LDFLAGS+=-Wl,--as-needed