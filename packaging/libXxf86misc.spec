%bcond_with x

Name:           libXxf86misc
Version:        1.0.3
Release:        6.5
License:        MIT
Summary:        X11 XFree86 miscellaneous extension library
Url:            http://www.x.org/
Group:          System/Libraries
Source0:        http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1001: 	libXxf86misc.manifest
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86miscproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

%description
X11 XFree86 miscellaneous extension library
libXxf86misc provides an interface to the XFree86-Misc extension, which allows client applications to query the current keyboard and mouse settings of the running XFree86-based (XFree86, Xorg) server.

More information about X.Org can be found at:
<URL:http://www.X.org>
<URL:http://xorg.freedesktop.org>
<URL:http://lists.freedesktop.org/mailman/listinfo/xorg>

This module can be found at
git://anongit.freedesktop.org/git/xorg/lib/libXxf86misc

%package devel
Summary:        X11 XFree86 miscellaneous extension library (development headers)
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X11 XFree86 miscellaneous extension library (development headers)
libXxf86misc provides an interface to the XFree86-Misc extension, which allows client applications to query the current keyboard and mouse settings of the running XFree86-based (XFree86, Xorg) server.

This package contains the development headers for the library found in libxxf86misc1.  Non-developers likely have little use for this package.

More information about X.Org can be found at:
<URL:http://www.X.org>
<URL:http://xorg.freedesktop.org>
<URL:http://lists.freedesktop.org/mailman/listinfo/xorg>

This module can be found at
git://anongit.freedesktop.org/git/xorg/lib/libXxf86misc

%prep
%setup -q
cp %{SOURCE1001} .


%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_libdir}/libXxf86misc.so.1
%{_libdir}/libXxf86misc.so.1.1.0


%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libXxf86misc.so
%{_libdir}/pkgconfig/xxf86misc.pc
%doc %{_mandir}/man3/*.3*

