Summary:	xteddy is a cuddly teddy bear for your X Windows desktop
Summary(pl):    xteddy to kochany pluszowy mi¶. Spotkasz go pod iXsami.
Name:		xteddy
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	http://www.ITN.LiU.SE/~stegu/xteddy/%{name}-1.1.tar.gz
URL:		http://www.ITN.LiU.SE/~stegu/xteddy/xteddy_info.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Normally, xteddy just sits around doing nothing. After all, that's
what teddy bears are for. Look at him, talk to him, place heavy
windows on top of him, zap him around until he becomes dizzy, do what
you like; he will always be your true (albeit virtual) friend.

%description -l pl 
Zwykle xteddy siedzi sobie nic nie robi±c, od tego w koñcu s± pluszowe
misie. Spójrz czasem na niego, zagadaj, przykryj ciep³ym okienkiem,
pobujaj (a¿ mu siê w g³owie zakrêci).  S³owem: pobaw siê z nim,
przecie¿ wszyscy kochamy pluszowe misie, prawda?

%prep
%setup -q

%build
%configure 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/X11/pixmaps,%{_mandir}/man1}
%{__make} install DESTDIR=$RPM_BUILD_ROOT 
strip $RPM_BUILD_ROOT%{_bindir}/%{name}
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1 {AUTHORS,README,xteddy.README}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xteddy
%{_includedir}/X11/pixmaps/*
%{_mandir}/man1/xteddy.1.gz
%doc {AUTHORS,README,xteddy.README}.gz

%clean
rm -rf $RPM_BUILD_ROOT
