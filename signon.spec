%define major 1
%define libextension %mklibname signon-extension %major
%define libplugins %mklibname signon-plugins-common %major
%define libqt %mklibname signon-qt %major
%define develextension %mklibname -d signon-extension
%define develplugins %mklibname -d signon-plugins-commo
%define develqt %mklibname -d signon-qt
%define develd %mklibname -d signond

Name:		signon
Version:	8.51
Release:	1	
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials
License:	LGPLv2
URL:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	doxygen

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n	%{libextension}
Group:		System/Libraries
Summary:	A framework for centrally storing authentication credentials

%description -n %{libextension}
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

%description -n %{develplugins}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	%{develqt}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libqt} = %{version}-%{release}

%description -n %{develqt}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{name}d
Summary:	A framework for centrally storing authentication credentials
Group:		System/Libraries

%description -n %{name}d
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package -n	%{develd}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}d = %{version}

%description -n %{develd}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation for %{name}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -q

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_sysconfdir}/signond.conf
%{_bindir}/signonpluginprocess
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

%files -n %{libplugins}
%{_libdir}/libsignon-plugins-common.so.%{major}
%{_libdir}/libsignon-plugins-common.so.%{major}.*

%files -n %{develplugins}
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.a
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_includedir}/signon-plugins

%files -n %{libqt}
%{_libdir}/libsignon-qt.so.%{major}
%{_libdir}/libsignon-qt.so.%{major}.*

%files -n %{develqt}
%{_libdir}/libsignon-qt.so
%{_libdir}/libsignon-qt.a
%{_libdir}/pkgconfig/libsignon-qt.pc
%{_includedir}/signon-qt
%{qt4dir}/mkspecs/features/*.prf

%files -n %{name}d
%{_bindir}/signond
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{develd}
%{_libdir}/pkgconfig/signond.pc
%{_includedir}/signond

%files doc
%{_datadir}/doc/libsignon-qt
%{_datadir}/doc/signon
%{_datadir}/doc/signon-plugins
%{_datadir}/doc/signon-plugins-dev
