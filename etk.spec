%define	name	etk
%define	version 0.1.0.003
%define release %mkrel 2

%define major   1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

#%define release 0.%{cvsrel}.%{mrelease}

%define cvsrel 20070516

%define major 	1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment toolkit
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
#BuildRequires:	ncurses-devel gtk-devel zlib-devel
BuildRequires:	multiarch-utils, ecore-devel >= 0.9.9.038, gettext-devel, cvs
BuildRequires: edje-devel >= 0.5.0.038, edje

%description
Etk is a toolkit based on the EFL libraries.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Requires: %name

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/etk_test
%{_bindir}/etk_prefs
%{_datadir}/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%{_libdir}/etk/engines/*.so

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%{_libdir}/etk/engines/*.a
%{_libdir}/etk/engines/*.la
%{_includedir}/*
%multiarch %{multiarch_bindir}/etk-config
%{_bindir}/etk-config
