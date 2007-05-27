Summary:	GNOME application launcher inspired by Quicksilver
Summary(pl.UTF-8):	Narzędzie GNOME do uruchamiania aplikacji zainspirowane Quicksilverem
Name:		gnome-launch-box
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ftp.imendio.com/pub/imendio/gnome-launch-box/src/%{name}-%{version}.tar.bz2
# Source0-md5:	fe905563933fc86081401dccae71e51c
URL:		http://developer.imendio.com/projects/gnome-launch-box/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	evolution-data-server-devel >= 1.8
BuildRequires:	gnome-desktop-devel >= 2.10
BuildRequires:	gnome-menus-devel >= 2.10
BuildRequires:	gnome-vfs2-devel >= 2.10
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launch Box is generally an application launcher. It's very influenced
by Quicksilver for Mac OS X. Remember that this is only a first
release so don't get your hopes up too much. Launch Box is written for
the GNOME 2.10 platform and depends on GTK+ 2.6, evolution-data-server 1.2
and gnome-menus. These are currently hard dependencies but the plan is
to split out the backends into different optional backends.

Currently supported modules are:
 - Application starting and launch
 - Evolution contacts lookup and mail to
 - Recent files lookup and open
 - Files in your desktop and open
 - Firefox bookmarks lookup and opening

%description -l pl.UTF-8
Launch Box to zasadniczo narzędzie do uruchamiania aplikacji. Jest w
dużym stopniu zainspirowane Quicksilverem dla Mac OS X. Należy
pamiętać, że jest to tylko pierwsze wydanie, więc nie należy
spodziewać się zbyt wiele. Launch Box został napisany dla platformy
GNOME 2.10, więc wymaga GTK+ 2.6, evolution-data-server 1.2 i
gnome-menus. Są to na razie sztywne zależności, ale są plany
wydzielenia opcjonalnych backendów.

Aktualnie obsługiwane moduły to:
 - Uruchamianie aplikacji
 - Wyszukiwanie kontaktów i pisanie listów w Evolution
 - Wyszukiwanie i otwieranie ostatnio używanych plików
 - Trzymanie i otwieranie plików na pulpicie
 - Wyszukiwanie i otwieranie zakładek Firefoksa

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-launch-box

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnome-launch-box
%dir %{_datadir}/lb
%dir %{_datadir}/lb/images
%{_datadir}/lb/images/*.png
%{_sysconfdir}/gconf/schemas/gnome-launch-box.schemas
