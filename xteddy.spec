Summary:	xteddy is a cuddly teddy bear for your X Window desktop
Summary(pl):	xteddy to kochany pluszowy mi¶, którego spotkasz pod X Window
Name:		xteddy
Version:	2.0.1
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.ITN.LiU.SE/~stegu/xteddy/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-automake.patch
URL:		http://www.ITN.LiU.SE/~stegu/xteddy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
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
pobujaj (a¿ mu siê w g³owie zakrêci). S³owem: pobaw siê z nim,
przecie¿ wszyscy kochamy pluszowe misie, prawda?

%prep
%setup -q
%patch -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements/

gzip -9nf AUTHORS README xteddy.README

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xteddy
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/xteddy
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
