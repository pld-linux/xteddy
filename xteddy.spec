Summary:	xteddy is a cuddly teddy bear for your X Window desktop
Summary(pl):	xteddy to kochany pluszowy mi¶, którego spotkasz pod X Window
Name:		xteddy
Version:	2.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.ITN.LiU.SE/~stegu/xteddy/%{name}-%{version}.tar.gz
# Source0-md5:	c197253b5116db5dc4e32b58dd36160e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-automake.patch
Patch1:		%{name}-icons.patch
URL:		http://www.ITN.LiU.SE/~stegu/xteddy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Amusements,%{_pixmapsdir}/%{name}/icons}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install images/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README xteddy.README
%attr(755,root,root) %{_bindir}/xteddy
%{_mandir}/man6/*
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
