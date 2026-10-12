%define oname GnuPGInterface

Summary:	GnuPG-Interface module for python
Name:		python-GnuPG-Interface
Version:	0.3.2
Release:	26
License:	LGPLv2
Group:		Development/Python
Url:		https://py-gnupg.sourceforge.net/
Source0:	http://py-gnupg.sourceforge.net/download/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	gnupg
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
This module provides Python bindings for the GnuPG.

%prep
%setup -qn %{oname}-%{version}
# distutils is gone. setuptools rejects the old "licence" keyword.
sed -i \
	-e 's/import distutils.core/import setuptools/' \
	-e 's/distutils.core.setup/setuptools.setup/' \
	-e 's/licence/license/' \
	setup.py
chmod 644 ./*

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc COPYING ChangeLog MANIFEST NEWS README THANKS
%{py_puresitedir}/GnuPGInterface.py*
%{py_puresitedir}/*.egg-info

