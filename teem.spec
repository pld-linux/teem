# TODO: levmar <http://www.ics.forth.gr/~lourakis/levmar/>
Summary:	Teem - tools to process and visualize scientific data and images
Summary(pl.UTF-8):	Teem - narzędzia do przetwarzania i wizualizacji danych i obrazów naukowych
Name:		teem
Version:	1.11.0
Release:	1
License:	SLUL v1 (LGPL v2.1+ with linking exception)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/teem/%{name}-%{version}-src.tar.gz
# Source0-md5:	6b9737e8b7640e18eaf281e830fe59d1
URL:		http://teem.sourceforge.net/
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.4
BuildRequires:	fftw3-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Teem - tools to process and visualize scientific data and images.

%description -l pl.UTF-8
Teem - narzędzia do przetwarzania i wizualizacji danych i obrazów
naukowych.

%package devel
Summary:	Header files for Teem library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Teem
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Teem library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Teem.

%prep
%setup -q -n %{name}-%{version}-src

%build
%cmake . \
	-DTeem_FFTW3=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/cmake/teem

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/teem

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%attr(755,root,root) %{_bindir}/gprobe
%attr(755,root,root) %{_bindir}/ilk
%attr(755,root,root) %{_bindir}/miter
%attr(755,root,root) %{_bindir}/mrender
%attr(755,root,root) %{_bindir}/nrrdSanity
%attr(755,root,root) %{_bindir}/overrgb
%attr(755,root,root) %{_bindir}/puller
%attr(755,root,root) %{_bindir}/tend
%attr(755,root,root) %{_bindir}/unu
%attr(755,root,root) %{_bindir}/vprobe
%attr(755,root,root) %{_libdir}/libteem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libteem.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libteem.so
%{_includedir}/teem
%{_libdir}/cmake/teem
