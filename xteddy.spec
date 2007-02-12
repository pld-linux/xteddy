Summary:	xteddy is a cuddly teddy bear for your X Window desktop
Summary(pl.UTF-8):	xteddy to kochany pluszowy miś, którego spotkasz pod X Window
Name:		xteddy
Version:	2.0.2
Release:	2
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

%description -l pl.UTF-8
Zwykle xteddy siedzi sobie nic nie robiąc, od tego w końcu są pluszowe
misie. Spójrz czasem na niego, zagadaj, przykryj ciepłym okienkiem,
pobujaj (aż mu się w głowie zakręci). Słowem: pobaw się z nim,
przecież wszyscy kochamy pluszowe misie, prawda?

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}/%{name}/icons}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install images/icons/* $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README xteddy.README
%attr(755,root,root) %{_bindir}/xteddy
%{_mandir}/man6/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
