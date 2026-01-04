#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_pkg dbus-1-tqt

%define libdbus %{_lib}dbus

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.9
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Dbus bindings for the Trinity Qt [TQt] interface
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/dependencies/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{_includedir}
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	libtqt3-mt-devel >= 3.5.0
BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0

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

%package -n %{libdbus}-1-tqt0
Summary:		Dbus bindings for the Trinity Qt [TQt] interface
Group:			System/Libraries
Provides:		libdbus-1-tqt0 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-dbus-1-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-1-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libdbus}-1-tqt0
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%post -n %{libdbus}-1-tqt0
/sbin/ldconfig || :

%postun -n %{libdbus}-1-tqt0
/sbin/ldconfig || :

%files -n %{libdbus}-1-tqt0
%defattr(-,root,root,-)
%{_libdir}/libdbus-1-tqt.so.0
%{_libdir}/libdbus-1-tqt.so.0.0.0

##########

%package -n %{libdbus}-1-tqt-devel
Summary:		Dbus bindings for the Trinity Qt [TQt] interface (Development Files)
Group:			Development/Libraries/C and C++
Provides:		libdbus-1-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{libdbus}-1-tqt0 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-dbus-1-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-1-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	dbus-devel

%description -n %{libdbus}-1-tqt-devel
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%post -n %{libdbus}-1-tqt-devel
/sbin/ldconfig || :

%postun -n %{libdbus}-1-tqt-devel
/sbin/ldconfig || :

%files -n %{libdbus}-1-tqt-devel
%defattr(-,root,root,-)
%{_bindir}/dbusxml2qt3
%{_includedir}/*.h
%{_libdir}/libdbus-1-tqt.so
%{_libdir}/libdbus-1-tqt.la
%{_libdir}/pkgconfig/*.pc

