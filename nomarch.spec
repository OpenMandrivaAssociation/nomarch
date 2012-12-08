Name:      nomarch
Summary:   GPLed Arc de-archiver 
Version:   1.4
Release:   %mkrel 7
URL:       http://rus.members.beeb.net/nomarch.html
License:   GPL
Source:    ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.bz2
Group:     Archiving/Compression
BuildRoot: %{_tmppath}/%{name}-root
Provides:  arc

%description
nomarch lists/extracts/tests `.arc' archives. (It also handles `.ark'
files, they're exactly the same.) This is a *very* outdated file
format which should never be used for anything new, but unfortunately,
you can still run into it every so often.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall_std BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc COPYING ChangeLog NEWS README TODO
%attr(0755, root, root) %_bindir/nomarch
%{_mandir}/man1/*



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-7mdv2011.0
+ Revision: 666618
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-6mdv2011.0
+ Revision: 606823
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-5mdv2010.1
+ Revision: 520193
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-4mdv2010.0
+ Revision: 426252
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2009.0
+ Revision: 223346
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.4-2mdv2008.1
+ Revision: 153284
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 22:05:15 (55205)
- add source

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 22:04:46 (55204)
- 1.4

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 22:02:46 (55203)
Import nomarch

* Fri Dec 30 2005 Olivier Thauvin <nanardon@mandriva.org> 1.3-3mdk
- rebuild

* Fri Dec 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3-2mdk
- Birthday rebuild

