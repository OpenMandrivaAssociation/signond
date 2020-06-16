%define major 1
%define libextension %mklibname signon-extension %major
%define libpluginscommon %mklibname signon-plugins-common %major
%define libplugins %mklibname signon-plugins %major
%define libqt %mklibname signon-qt5 %major
%define develextension %mklibname -d signon-extension
%define develplugins %mklibname -d signon-plugins-common
%define develqt %mklibname -d signon-qt
%define develd %mklibname -d signond
# signond doesn't seem to make releases anymore
%define snapshot 20200616

Name:		signond
Version:	8.60
Release:	0.%{snapshot}.1
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
URL:		http://gitlab.com/accounts-sso/
# git clone https://gitlab.com/accounts-sso/signond.git
# git archive --format=tar --prefix signond-8.60/ HEAD | xz -9 > signond-8.60-$(date +%Y%m%d).tar.xz
Source0:	signond-%{version}-%{snapshot}.tar.xz
Patch1:		signon-8.57-no_static.patch
BuildRequires:	qt5-devel
BuildRequires:	qt5-qttools
BuildRequires:	qt5-qttools-qtdbus
BuildRequires:	qt5-assistant
BuildRequires:	qt5-designer
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:	cmake(Qt5Test)
BuildRequires:	qtchooser
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

%description -n %{libextension}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libpluginscommon}
Group: System/Libraries
Summary: A framework for centrally storing authentication credentials

%description -n %{libpluginscommon}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libplugins}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials

%description -n %{libplugins}
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n %{libqt}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials

%description -n %{libqt}
Single Sign-On is a framework for centrally storing authentication credentials
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
%setup -qn %{name}-%{version}
%autopatch -p1

sed -i 's/qdbusxml2cpp/qdbusxml2cpp-qt5/' src/signond/signond.pro

%build
%qmake_qt5 CONFIG+=debug_and_release LIBDIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_sysconfdir}/signond.conf
%{_bindir}/signonpluginprocess
%{_bindir}/signond
%dir %{_libdir}/signon
%{_libdir}/signon/*.so
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml

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

%files -n %{develd}
%{_libdir}/pkgconfig/signond.pc
%{_includedir}/signond

%files doc
%{_datadir}/doc/libsignon-qt
%{_datadir}/doc/signon
%{_datadir}/doc/signon-plugins
%{_datadir}/doc/signon-plugins-dev
