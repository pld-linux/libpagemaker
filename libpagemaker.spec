#
# Conditional build:
%bcond_without	static_libs	# static library
#
%define		apiversion	0.1
Summary:	Library for importing and converting PageMaker documents
Summary(pl.UTF-8):	Biblioteka do importowania i konwersji dokumentów PageMakera
Name:		libpagemaker
Version:	0.0.0
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libpagemaker/%{name}-%{version}.tar.xz
# Source0-md5:	45e2ca30ce6a089fe0fec4badd636632
URL:		https://wiki.documentfoundation.org/DLP/Libraries/libpagemaker
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf >= 3.0.0
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpagemaker is a library for importing and converting of PageMaker
documents.

%description -l pl.UTF-8
libpagemaker to biblioteka do importowaniai konwersji dokumentów
PageMakera.

%package devel
Summary:	Development files for libpagemaker
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libpagemaker
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	zlib-devel

%description devel
This package contains the header files for developing applications
that use libpagemaker.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki i pliki nagłówkowe do tworzenia
aplikacji wykorzystujących bibliotekę libpagemaker.

%package static
Summary:	Static libpagemaker library
Summary(pl.UTF-8):	Statyczna biblioteka libpagemaker
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpagemaker library.

%description static -l pl.UTF-8
Statyczna biblioteka libpagemaker.

%package apidocs
Summary:	API documentation for libpagemaker library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libpagemaker
Group:		Documentation

%description apidocs
API documentation for libpagemaker library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libpagemaker.

%package tools
Summary:	Tools to transform PageMaker files into other formats
Summary(pl.UTF-8):	Narzędzia do przekształcania plików PageMakera do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform PageMaker files into other formats. Currently
supported: SVG, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania plików PageMakera do innych formatów.
Obecnie obsługiwane są: SVG i surowy.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# we install API docs directly from build
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS NOTES
%attr(755,root,root) %{_libdir}/libpagemaker-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpagemaker-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpagemaker-0.0.so
%{_includedir}/libpagemaker-0.0
%{_pkgconfigdir}/libpagemaker-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpagemaker-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pmd2raw
%attr(755,root,root) %{_bindir}/pmd2svg
