%define major 5
%define devname %mklibname milou -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230726

Name: plasma6-milou
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/milou/-/archive/master/milou-master.tar.bz2#/milou-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: A search client for Baloo
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
# Just to make sure we don't pull in Plasma 5
BuildRequires: plasma6-xdg-desktop-portal-kde

%description
A search client for Baloo.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Milou search library
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Milou search library.

%prep
%autosetup -p1 -n milou-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang milou
%find_lang plasma_applet_org.kde.milou

%files -f milou.lang -f plasma_applet_org.kde.milou.lang
%{_qtdir}/qml/org/kde/milou
%{_datadir}/plasma/plasmoids/org.kde.milou
%{_datadir}/metainfo/org.kde.milou.appdata.xml
