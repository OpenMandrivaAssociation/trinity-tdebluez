#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define tde_pkg tdebluez
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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
Version:	1.0.8
Release:	%{?tde_version}_%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE Bluetooth Framework
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildRequires:  cmake make
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


BuildRequires:	trinity-tde-cmake >= %{tde_version}
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  trinity-dbus-1-tqt-devel


%description
The TDE Bluetooth Framework is a set of tools built on top of Linux' Bluetooth
stack BlueZ5. It provides easy access to the most common Bluetooth profiles and
makes data exchange with Bluetooth devices like phones and PDAs as
straightforward as possible.

Features:
* tdebluez -- a tray applet to handle incoming inquiries and control
              adapters and devices
* tdebluezauth -- authentication agent
* tdeioclient -- cli to obex

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/tdebluez
%{tde_bindir}/tdebluezauth
%{tde_bindir}/tdebluezioclient
%{tde_libdir}/libtdeinit_tdebluez.so
%{tde_libdir}/libtdeinit_tdebluez.la
%{tde_tdelibdir}/tdebluez.so
%{tde_tdelibdir}/tdebluez.la
%{tde_tdelibdir}/tdeio_bluetooth.so
%{tde_tdelibdir}/tdeio_bluetooth.la
%{tde_tdelibdir}/tdeio_obex.so
%{tde_tdelibdir}/tdeio_obex.la
%{tde_tdedocdir}/HTML/*
%{tde_datadir}/apps/tdebluez/
%{tde_tdeappdir}/tdebluez.desktop
%{tde_tdeappdir}/tdebluezauth.desktop
%{tde_datadir}/autostart/tdebluez.autostart.desktop
%{tde_datadir}/icons/hicolor/*/apps/tdebluez.png
%{tde_datadir}/icons/hicolor/scalable/apps/tdebluez.svgz
%{tde_datadir}/mimelnk/bluetooth/*
%{tde_datadir}/services/bluetooth.protocol
%{tde_datadir}/services/obexftp.protocol
%{tde_datadir}/services/obexopp.protocol
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/bluetooth_sidebarentry.desktop
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/obex_sidebarentry.desktop
%{_sysconfdir}/dbus-1/system.d/org.trinitydesktop.tdebluez.conf


##########

%package -n trinity-libtdebluez
Summary:	Bluetooth library for TDE

%description -n trinity-libtdebluez
This package is part of the TDE Bluetooth Framework.
It contains a Bluetooth library for TDE.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdebluez
%defattr(-,root,root,-)
%{tde_libdir}/libtdebluez.la
%{tde_libdir}/libtdebluez.so.*

##########

%package -n trinity-libtdeobex
Summary:	Obex library for TDE

%description -n trinity-libtdeobex
This package is part of the TDE Bluetooth Framework.
It contains a Bluetooth library for TDE.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdeobex
%defattr(-,root,root,-)
%{tde_libdir}/libtdeobex.la
%{tde_libdir}/libtdeobex.so.*

##########

%package -n trinity-libtdebluez-devel
Summary:	Development files for libtdebluez

%description -n trinity-libtdebluez-devel
This package is part of the TDE Bluetooth Framework.
It contains the development files for libtdebluez.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdebluez-devel
%defattr(-,root,root,-)
%{tde_includedir}/tdebluez/*
%{tde_libdir}/libtdebluez.so
%{tde_datadir}/cmake/libtdebluez.cmake

##########

%package -n trinity-libtdeobex-devel
Summary:	Development files for libtdeobex

%description -n trinity-libtdeobex-devel
This package is part of the TDE Bluetooth Framework.
It contains the development files for libtdeobex.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdeobex-devel
%defattr(-,root,root,-)
%{tde_includedir}/tdeobex/*
%{tde_libdir}/libtdeobex.so
%{tde_datadir}/cmake/libtdeobex.cmake

##########

%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%autosetup -n %{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_includedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DBUILD_ALL=ON \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}

