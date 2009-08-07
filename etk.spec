%define	name	etk
%define version 0.1.0.042
%define svnrel	20090503
%define release %mkrel 7.%{svnrel}.4

%define major   1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightenment toolkit
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.bz2
Patch0:		etk-0.1.0.042-fix-linkage.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.060
Buildrequires:	eet-devel
BuildRequires:	edje-devel >= 0.5.0.042, edje => 0.5.0.042
Buildrequires:	embryo >= 0.9.9.050, embryo-devel >= 0.9.9.050
Buildrequires:	gettext-devel

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
%setup -qn %name
%patch0 -p0

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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
