#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liblogging
Version  : 1.0.6
Release  : 4
URL      : https://github.com/rsyslog/liblogging/archive/v1.0.6.tar.gz
Source0  : https://github.com/rsyslog/liblogging/archive/v1.0.6.tar.gz
Summary  : an enhanced replacement for the syslog() API with admin-configurable destinations
Group    : Development/Tools
License  : BSD-2-Clause
Requires: liblogging-bin = %{version}-%{release}
Requires: liblogging-lib = %{version}-%{release}
Requires: liblogging-license = %{version}-%{release}
Requires: liblogging-man = %{version}-%{release}
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pypi-docutils

%description


%package bin
Summary: bin components for the liblogging package.
Group: Binaries
Requires: liblogging-license = %{version}-%{release}

%description bin
bin components for the liblogging package.


%package dev
Summary: dev components for the liblogging package.
Group: Development
Requires: liblogging-lib = %{version}-%{release}
Requires: liblogging-bin = %{version}-%{release}
Provides: liblogging-devel = %{version}-%{release}
Requires: liblogging = %{version}-%{release}

%description dev
dev components for the liblogging package.


%package lib
Summary: lib components for the liblogging package.
Group: Libraries
Requires: liblogging-license = %{version}-%{release}

%description lib
lib components for the liblogging package.


%package license
Summary: license components for the liblogging package.
Group: Default

%description license
license components for the liblogging package.


%package man
Summary: man components for the liblogging package.
Group: Default

%description man
man components for the liblogging package.


%prep
%setup -q -n liblogging-1.0.6
cd %{_builddir}/liblogging-1.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649966808
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1649966808
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liblogging
cp %{_builddir}/liblogging-1.0.6/COPYING %{buildroot}/usr/share/package-licenses/liblogging/2942615ee26f9c8c1380d34e6ac7c3210c551437
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stdlogctl

%files dev
%defattr(-,root,root,-)
/usr/include/liblogging/stdlog.h
/usr/lib64/liblogging-stdlog.so
/usr/lib64/pkgconfig/liblogging-stdlog.pc
/usr/share/man/man3/stdlog.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblogging-stdlog.so.0
/usr/lib64/liblogging-stdlog.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liblogging/2942615ee26f9c8c1380d34e6ac7c3210c551437

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/stdlogctl.1
