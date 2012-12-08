%define name python-GnuPG-Interface
%define version 0.3.2
%define release %mkrel 12
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





%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-10mdv2011.0
+ Revision: 667910
- mass rebuild

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 0.3.2-9mdv2011.0
+ Revision: 593346
- update file list

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdv2010.1
+ Revision: 523760
- rebuilt for 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-7mdv2010.0
+ Revision: 442140
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.3.2-6mdv2009.1
+ Revision: 323527
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-5mdv2009.0
+ Revision: 259619
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-4mdv2009.0
+ Revision: 247423
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-2mdv2008.1
+ Revision: 139212
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.2-1mdv2007.0
+ Revision: 91374
- Rebuild against new python
- import python-GnuPG-Interface-0.3.2-1mdk

* Thu May 04 2006 Jerome Martin <jmartin@mandriva.org> 0.3.2-1mdk
- Initial version

