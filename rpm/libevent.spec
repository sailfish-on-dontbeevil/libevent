Name:           libevent
Version:        2.1.8
Release:        1
Summary:        An event notification library
License:        BSD
URL:            http://libevent.org/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires: gcc doxygen openssl-devel
BuildRequires: automake libtool
Patch0: libevent-nonettests.patch
Patch1: http-callback.patch

%description
Libevent additionally provides a sophisticated framework for buffered network IO, with support for sockets,
filters, rate-limiting, SSL, zero-copy file transmission, and IOCP.
Libevent includes support for several useful protocols, including DNS, HTTP, and a minimal RPC framewor.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --disable-dependency-tracking --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc ChangeLog
%license LICENSE
%{_libdir}/libevent-2.1.so.*
%{_libdir}/libevent_core-2.1.so.*
%{_libdir}/libevent_extra-2.1.so.*
%{_libdir}/libevent_openssl-2.1.so.*
%{_libdir}/libevent_pthreads-2.1.so.*

%files devel
%{_includedir}/*.h
%dir %{_includedir}/event2
%{_includedir}/event2/*.h
%{_libdir}/libevent.so
%{_libdir}/libevent_core.so
%{_libdir}/libevent_extra.so
%{_libdir}/libevent_openssl.so
%{_libdir}/libevent_pthreads.so
%{_libdir}/pkgconfig/libevent.pc
%{_libdir}/pkgconfig/libevent_core.pc
%{_libdir}/pkgconfig/libevent_extra.pc
%{_libdir}/pkgconfig/libevent_openssl.pc
%{_libdir}/pkgconfig/libevent_pthreads.pc
%{_bindir}/event_rpcgen.*
