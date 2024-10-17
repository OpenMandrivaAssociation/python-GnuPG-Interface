%define oname GnuPGInterface

Summary:	GnuPG-Interface module for python
Name:		python-GnuPG-Interface
Version:	0.3.2
Release:	23
License:	LGPLv2
Group:		Development/Python
Url:		https://py-gnupg.sourceforge.net/
Source0:	http://py-gnupg.sourceforge.net/download/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	gnupg
BuildRequires:	pkgconfig(python)

%description
This module provides Python bindings for the GnuPG.

%prep
%setup -qn %{oname}-%{version}
chmod 644 ./*

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc COPYING ChangeLog MANIFEST NEWS README THANKS
%{py_puresitedir}/GnuPGInterface.py*
%{py_puresitedir}/*.egg-info

