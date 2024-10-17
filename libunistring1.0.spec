%define major 2
%define libname %mklibname unistring %{major}

%global optflags %{optflags} -O3

Summary:	Old version of the GNU Unicode string library
Name:		libunistring1.0
Version:	1.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnu.org/software/libunistring/
Source0:	http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz
Patch0:		libunistring-1.0-attribute-dealloc-clang.patch
BuildRequires:	slibtool

%description
This is an old version of the unistring library, provided for compatibility
with legacy applications only.

This library implements Unicode strings (in three flavours: UTF-8
strings, UTF-16 strings, UTF-32 strings), together with functions for
Unicode charactets (character names, classifications, properties) and
functions for string processing (formatted output, width, word breaks,
line breaks, normalization, case folding, regular expressions).

%package -n %{libname}
Group:		System/Libraries
Summary:	GNU Unicode string library

%description -n %{libname}
This is an old version of the unistring library, provided for compatibility
with legacy applications only.

This library implements Unicode strings (in three flavours: UTF-8
strings, UTF-16 strings, UTF-32 strings), together with functions for
Unicode charactets (character names, classifications, properties) and
functions for string processing (formatted output, width, word breaks,
line breaks, normalization, case folding, regular expressions).

%prep
%autosetup -p1 -n libunistring-%{version}
rm -f m4/libtool.m4 m4/lt*.m4
./autogen.sh --skip-gnulib

export CONFIGURE_TOP="$(pwd)"

mkdir build
cd build
%configure \
	--enable-static

%build
%make_build -C build LIBTOOL=slibtool-shared

%install
%make_install -C build LIBTOOL=slibtool-shared
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/libunistring.so \
	%{buildroot}%{_docdir}/libunistring \
	%{buildroot}%{_infodir}/libunistring.info*

%files -n %{libname}
%{_libdir}/libunistring.so.%{major}*
