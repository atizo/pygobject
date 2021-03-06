AUTOMAKE_OPTIONS = 1.7

PLATFORM_VERSION = 2.0

INCLUDES = 				\
	$(PYTHON_INCLUDES) 		\
	$(PYGOBJECT_CFLAGS)		\
	$(GIO_CFLAGS)			\
	-I$(top_srcdir)/gobject

# defs files
defsdir = $(pkgdatadir)/$(PLATFORM_VERSION)/defs
defs_DATA =

# python
pyexec_LTLIBRARIES =

# gio extension modules
pkgpyexecdir = $(pyexecdir)/gtk-2.0/gio
pkgpyexec_LTLIBRARIES =

# gio python scripts
pygiodir = $(pkgpyexecdir)
pygio_PYTHON = 	__init__.py

# linker flags
common_ldflags = -module -avoid-version
if PLATFORM_WIN32
common_ldflags += -no-undefined
endif

CLEANFILES =
EXTRA_DIST = 

# gio module
GIO_OVERRIDES = 			\
	gappinfo.override		\
	gio.override			\
	gfile.override			\
	gfileenumerator.override	\
	gfileinfo.override		\
	ginputstream.override 		\
	goutputstream.override 		\
	gvolumemonitor.override

GIO_DEFS = gio.defs gio-types.defs $(GIO_OVERRIDES)
CLEANFILES += gio.c
EXTRA_DIST += $(GIO_DEFS) $(GIO_OVERRIDES)
gio.c: $(GIO_DEFS) $(GIO_OVERRIDES)
_gio_la_CFLAGS = $(GIO_CFLAGS)
_gio_la_LDFLAGS = $(common_ldflags) -export-symbols-regex init_gio
_gio_la_LIBADD = $(GIO_LIBS)
_gio_la_SOURCES = \
	giomodule.c \
	pygio-utils.c \
	pygio-utils.h
nodist__gio_la_SOURCES = gio.c
if BUILD_GIO
pkgpyexec_LTLIBRARIES += _gio.la
defs_DATA += $(GIO_DEFS)
endif

# giounix module
GIOUNIX_DEFS = unix.defs unix-types.defs unix.override
CLEANFILES += unix.c
EXTRA_DIST += $(GIOUNIX_DEFS) unix.override
giounix.c: $(GIOUNIX_DEFS) unix.override
unix_la_CFLAGS = $(GIOUNIX_CFLAGS)
unix_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initunix
unix_la_LIBADD = $(GIOUNIX_LIBS)
unix_la_SOURCES = unixmodule.c
nodist_unix_la_SOURCES = unix.c
if BUILD_GIOUNIX
pkgpyexec_LTLIBRARIES += unix.la
defs_DATA += $(GIOUNIX_DEFS)
endif


# code generator
.defs.c:
	(cd $(srcdir)\
	 && $(PYTHON) $(top_srcdir)/codegen/codegen.py \
	    --py_ssize_t-clean \
	    --register gio-types.defs \
	    --register unix-types.defs \
	    --override $*.override \
	    --prefix py$(*F) $*.defs) > $(*D)/gen-$(*F).c \
	&& cp $(*D)/gen-$(*F).c $(*D)/$(*F).c \
	&& rm -f $(*D)/gen-$(*F).c

