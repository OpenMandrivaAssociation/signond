%define major 1
%define oldlibextension %mklibname signon-extension 1
%define libextension %mklibname signon-extension
%define oldlibpluginscommon %mklibname signon-plugins-common 1
%define libpluginscommon %mklibname signon-plugins-common
%define oldlibplugins %mklibname signon-plugins 1
%define libplugins %mklibname signon-plugins
%define oldlibqt %mklibname signon-qt5 1
%define libqt %mklibname signon-qt5
%define libqt6 %mklibname signon-qt6
%define develextension %mklibname -d signon-extension
%define develplugins %mklibname -d signon-plugins-common
%define develqt %mklibname -d signon-qt
%define develqt6 %mklibname -d signon-qt6
%define develd %mklibname -d signond
# signond doesn't seem to make releases anymore
%define snapshot 20240113

Name:		signond
Version:	8.62
Release:	1
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
# Original version: https://gitlab.com/accounts-sso/signond
# But the fork is better and more actively maintained.
URL:		https://gitlab.com/nicolasfella/signond/
%if 0%{?snapshot:1}
Source0:	https://gitlab.com/nicolasfella/signond/-/archive/qt6/signond-qt6.tar.bz2
%else
Source0:	https://gitlab.com/nicolasfella/signond/-/archive/VERSION_%{version}/signond-VERSION_%{version}.tar.bz2
%endif
Patch1:		signon-8.57-no_static.patch
BuildRequires:	qt5-devel
BuildRequires:	qt5-qttools
BuildRequires:	qt5-qttools-qtdbus
BuildRequires:	qt5-assistant
BuildRequires:	qt5-designer
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	qtchooser

BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	qmake-qt6

BuildRequires:	doxygen
BuildRequires:	graphviz
%rename	signon
Requires:	dbus
Suggests:	signon-ui

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libextension}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
%rename %{oldlibextension}

%description -n %{libextension}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libpluginscommon}
Group: System/Libraries
Summary: A framework for centrally storing authentication credentials
%rename %{oldlibpluginscommon}

%description -n %{libpluginscommon}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libplugins}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
%rename %{oldlibplugins}

%description -n %{libplugins}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libqt}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
%rename %{oldlibqt}

%description -n %{libqt}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libqt6}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials for Qt 6

%description -n %{libqt6}
Single Sign-On is a framework for Qt 6 for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{develextension}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libextension} = %{version}-%{release}

%description -n %{develextension}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{develplugins}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libplugins} = %{version}-%{release}
Requires:	%{libpluginscommon} = %{version}-%{release}
Obsoletes:	%{mklibname -d signon-plugins-commo}

%description -n %{develplugins}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{develqt}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libqt} = %{version}-%{release}

%description -n %{develqt}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{develqt6}
Summary:	Development files for %{name} for Qt 6
Group:		Development/C
Requires:	%{libqt6} = %{version}-%{release}

%description -n %{develqt6}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} with Qt 6.

%package -n %{develd}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description -n %{develd}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -qn %{name}-%{?snapshot:qt6}%{!?snapshot:VERSION_%{version}}
%autopatch -p1

mkdir qt5
mv $(ls -1 |grep -vE '^qt5$') .* qt5/
cp -a qt5 qt6

sed -i 's/qdbusxml2cpp/qdbusxml2cpp-qt5/' qt5/src/signond/signond.pro

%build
cd qt5
%qmake_qt5 CONFIG+=debug_and_release LIBDIR=%{_libdir}
%make_build

cd ../qt6
%{_qtdir}/bin/qmake CONFIG+=debug_and_release LIBDIR=%{_libdir}
%make_build

%install
cd qt5
%make_install INSTALL_ROOT=%{buildroot}

cd ../qt6
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_sysconfdir}/signond.conf
%{_bindir}/signonpluginprocess
%{_bindir}/signond
%dir %{_libdir}/signon
%{_libdir}/signon/*.so
%{_datadir}/dbus-1/services/*.service

%files -n %{libextension}
%{_libdir}/libsignon-extension.so.%{major}
%{_libdir}/libsignon-extension.so.%{major}.*

%files -n %{develextension}
%{_libdir}/libsignon-extension.so
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_includedir}/signon-extension

%files -n %{libpluginscommon}
%{_libdir}/libsignon-plugins-common.so.%{major}
%{_libdir}/libsignon-plugins-common.so.%{major}.*

%files -n %{libplugins}
%{_libdir}/libsignon-plugins.so.%{major}
%{_libdir}/libsignon-plugins.so.%{major}.*

%files -n %{develplugins}
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_includedir}/signon-plugins

%files -n %{libqt}
%{_libdir}/libsignon-qt5.so.%{major}
%{_libdir}/libsignon-qt5.so.%{major}.*

%files -n %{develqt}
%{_libdir}/libsignon-qt5.so
%{_libdir}/pkgconfig/libsignon-qt5.pc
%{_includedir}/signon-qt5
#% {qt4dir}/mkspecs/features/*.prf
%{_libdir}/cmake/SignOnQt5

%files -n %{libqt6}
%{_libdir}/libsignon-qt6.so.%{major}*

%files -n %{develqt6}
%{_libdir}/libsignon-qt6.so
%{_includedir}/signon-qt6
%{_libdir}/cmake/SignOnQt6
%{_libdir}/pkgconfig/libsignon-qt6.pc

%files -n %{develd}
%{_libdir}/pkgconfig/signond.pc
%{_includedir}/signond

%files doc
%{_datadir}/doc/libsignon-qt
%{_datadir}/doc/signon
%{_datadir}/doc/signon-plugins
%{_datadir}/doc/signon-plugins-dev
