# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       krunner

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 module for KRunner
Version:    5.3.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  krunner.yaml
Source101:  krunner-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kservice-devel
BuildRequires:  plasma-devel
BuildRequires:  solid-devel
BuildRequires:  threadweaver-devel

%description
KDE Frameworks 5 Tier 3 module for KRunner.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   kcoreaddons-devel
Requires:   ki18n-devel
Requires:   kservice-devel
Requires:   plasma-devel
Requires:   solid-devel
Requires:   threadweaver-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc README.md
%{_kf5_libdir}/libKF5Runner.so.*
%{_kf5_qmldir}/org/kde/runnermodel
%{_kf5_servicetypesdir}/plasma-runner.desktop
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/krunner_version.h
%{_kf5_includedir}/KRunner
%{_kf5_libdir}/libKF5Runner.so
%{_kf5_cmakedir}/KF5Runner
%{_kf5_mkspecsdir}/qt_KRunner.pri
# >> files devel
# << files devel
