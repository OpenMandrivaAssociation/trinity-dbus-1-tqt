# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg dbus-1-tqt

%define libname %mklibname %{tde_pkg}
%define devname %mklibname %{tde_pkg} -d

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.9
Release:	%{?tde_version:%{tde_version}_}5
Summary:	Dbus bindings for the Trinity Qt [TQt] interface
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/dependencies/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{_includedir}
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	pkgconfig(tqt-mt)
BuildRequires:	pkgconfig(tqt)

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# DBUS support
BuildRequires:  pkgconfig(dbus-1)


%description
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

###########

%package -n %{libname}0
Summary:		Dbus bindings for the Trinity Qt [TQt] interface
Group:			System/Libraries

%description -n %{libname}0
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%files -n %{libname}0
%defattr(-,root,root,-)
%{_libdir}/libdbus-1-tqt.so.0
%{_libdir}/libdbus-1-tqt.so.0.0.0

##########

%package -n %{devname}
Summary:		Dbus bindings for the Trinity Qt [TQt] interface (Development Files)
Group:			Development/Libraries/C and C++

Requires:		%{libname}0 = %{EVRD}

Requires:	dbus-devel

%description -n %{devname}
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%files -n %{devname}
%defattr(-,root,root,-)
%{_bindir}/dbusxml2qt3
%{_includedir}/*.h
%{_libdir}/libdbus-1-tqt.so
%{_libdir}/libdbus-1-tqt.la
%{_libdir}/pkgconfig/*.pc

