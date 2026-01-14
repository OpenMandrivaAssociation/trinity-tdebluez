%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdebluez
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0.8
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	TDE Bluetooth Framework
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo" 
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}


BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)


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
%{tde_prefix}/bin/tdebluez
%{tde_prefix}/bin/tdebluezauth
%{tde_prefix}/bin/tdebluezioclient
%{tde_prefix}/%{_lib}/libtdeinit_tdebluez.so
%{tde_prefix}/%{_lib}/libtdeinit_tdebluez.la
%{tde_prefix}/%{_lib}/trinity/tdebluez.so
%{tde_prefix}/%{_lib}/trinity/tdebluez.la
%{tde_prefix}/%{_lib}/trinity/tdeio_bluetooth.so
%{tde_prefix}/%{_lib}/trinity/tdeio_bluetooth.la
%{tde_prefix}/%{_lib}/trinity/tdeio_obex.so
%{tde_prefix}/%{_lib}/trinity/tdeio_obex.la
%{tde_prefix}/share/doc/tde/HTML/*
%{tde_prefix}/share/apps/tdebluez/
%{tde_prefix}/share/applications/tde/tdebluez.desktop
%{tde_prefix}/share/applications/tde/tdebluezauth.desktop
%{tde_prefix}/share/autostart/tdebluez.autostart.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/tdebluez.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/tdebluez.svgz
%{tde_prefix}/share/mimelnk/bluetooth/*
%{tde_prefix}/share/services/bluetooth.protocol
%{tde_prefix}/share/services/obexftp.protocol
%{tde_prefix}/share/services/obexopp.protocol
%{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/bluetooth_sidebarentry.desktop
%{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/obex_sidebarentry.desktop
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
%{tde_prefix}/%{_lib}/libtdebluez.la
%{tde_prefix}/%{_lib}/libtdebluez.so.*

##########

%package -n trinity-libtdeobex
Summary:	Obex library for TDE

%description -n trinity-libtdeobex
This package is part of the TDE Bluetooth Framework.
It contains a Bluetooth library for TDE.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdeobex
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libtdeobex.la
%{tde_prefix}/%{_lib}/libtdeobex.so.*

##########

%package -n trinity-libtdebluez-devel
Summary:	Development files for libtdebluez

%description -n trinity-libtdebluez-devel
This package is part of the TDE Bluetooth Framework.
It contains the development files for libtdebluez.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdebluez-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tdebluez/*
%{tde_prefix}/%{_lib}/libtdebluez.so
%{tde_prefix}/share/cmake/libtdebluez.cmake

##########

%package -n trinity-libtdeobex-devel
Summary:	Development files for libtdeobex

%description -n trinity-libtdeobex-devel
This package is part of the TDE Bluetooth Framework.
It contains the development files for libtdeobex.

See the 'trinity-tdebluez' package for more informations.

%files -n trinity-libtdeobex-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tdeobex/*
%{tde_prefix}/%{_lib}/libtdeobex.so
%{tde_prefix}/share/cmake/libtdeobex.cmake


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg}

