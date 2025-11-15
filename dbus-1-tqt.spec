#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg dbus-1-tqt

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libdbus %{_lib}dbus
%else
%define libdbus libdbus
%endif

%if 0%{?mdkversion}
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)



Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.9
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Dbus bindings for the Trinity Qt [TQt] interface
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/dependencies/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildRequires:  cmake make

BuildRequires:	libtqt3-mt-devel >= 3.5.0
BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0

BuildRequires:	trinity-tde-cmake >= %{tde_version}
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
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

%if 0%{?suse_version}
Requires:	dbus-1-devel
%else
Requires:	dbus-devel
%endif

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

##########

%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{_bindir} \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__make install DESTDIR=%{?buildroot} -C build

