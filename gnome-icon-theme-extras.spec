Summary:	Additional icons for GNOME environment
Summary(pl.UTF-8):	Dodatkowe ikony dla środowiska GNOME
Name:		gnome-icon-theme-extras
Version:	2.90.7
Release:	1
License:	CC-BY-SA
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme-extras/2.90/%{name}-%{version}.tar.bz2
# Source0-md5:	366e002d712b5c4a0b62105c87813f69
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.601
Requires:	gtk-update-icon-cache
Requires:	gnome-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains additional device and MIME-type icons for use by
the GNOME desktop.

%description -l pl.UTF-8
Ten pakiet zawiera dodatkowe ikony urządzeń i typów MIME używanych
przez środowisko GNOME.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome

%postun
%update_icon_cache gnome

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_iconsdir}/gnome/*/*/*.png
