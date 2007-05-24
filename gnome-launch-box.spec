#
Summary:	GNOME application launcher inspired by Quicksilver
Name:		gnome-launch-box
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://ftp.imendio.com/pub/imendio/gnome-launch-box/src/%{name}-%{version}.tar.bz2
# Source0-md5:	fe905563933fc86081401dccae71e51c
URL:		http://developer.imendio.com/projects/gnome-launch-box/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnome-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launch Box is generally an application launcher. It's very influenced
by Quicksilver for Mac OSX. Remember that this is only a first release
so don't get your hopes up too much. Launch Box is written for the
GNOME 2.10 platform and depends on GTK+ 2.6, evolution-data-server 1.2
and gnome-menus. These are currently hard dependencies but the plan is
to split out the backends into different optional backends.

Currently supported modules are:

    - Application starting and launch
    - Evolution contacts lookup and mail to
    - Recent files lookup and open
    - Files in your desktop and open
    - Firefox bookmarks lookup and opening


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
%{_sysconfdir}/gconf/schemas/gnome-launch-box.schemas
%attr(755,root,root) %{_bindir}/gnome-launch-box
%dir %{_datadir}/lb/
%dir %{_datadir}/lb/images/
%{_datadir}/lb/images/*.png
