Name:      nomarch
Summary:   GPLed Arc de-archiver 
Version:   1.4
Release:   %mkrel 2
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

