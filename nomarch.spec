Summary:	GPLed Arc de-archiver 
Name:		nomarch
Version:	1.4
Release:	10
Group:		Archiving/Compression
License:	GPLv2
Url:		http://rus.members.beeb.net/nomarch.html
Source0:	ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.bz2
Provides:	arc

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
%makeinstall_std \
	BINDIR=%{buildroot}/%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc COPYING ChangeLog NEWS README TODO
%{_bindir}/nomarch
%{_mandir}/man1/*

