%define name python-GnuPG-Interface
%define version 0.3.2
%define release %mkrel 10
%define oname GnuPGInterface

Summary: GnuPG-Interface module for python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://py-gnupg.sourceforge.net/download/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://py-gnupg.sourceforge.net/
BuildRequires: python-devel
BuildRequires:  gnupg
BuildArch:	noarch

%description
This module provides Python bindings for the GnuPG.

%prep
%setup -q -n %oname-%version
chmod 644 ./*

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf %buildroot 
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING ChangeLog MANIFEST NEWS README THANKS
%{py_puresitedir}/GnuPGInterface.py*
%{py_puresitedir}/*.egg-info



