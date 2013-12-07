%define		vermain		4.0b
#define		verminor	5
Summary:	Bigloo is compiler for the Scheme programming language
Summary(pl.UTF-8):	Bigloo - kompilator języka programowania Scheme
Name:		bigloo
#Version:	%{vermain}.%{verminor}
Version:	%{vermain}
Release:	1
License:	GPL/LGPL
Group:		Development/Languages
#Source0:	ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/%{name}%{vermain}-%{verminor}.tar.gz
Source0:	ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/%{name}%{vermain}.tar.gz
# Source0-md5:	5e66d9516a877f2b892d191bbe809379
Patch0:		%{name}-install.patch
URL:		http://www-sop.inria.fr/mimosa/fp/Bigloo/
BuildRequires:	gmp-devel
BuildRequires:	openssl-devel
BuildRequires:	sqlite3-devel
BuildRequires:	gstreamer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigloo is a compiler and interpreter for an extended version of the
Scheme programming language. Bigloo allows a full connection between
Scheme and C programs. It delivers fast and small executables.

%description -l pl.UTF-8
Bigloo jest kompilatorem i interpreterem rozszerzonej wersji języka
programowania Scheme. Bigloo pozwala na pełne łączenie programów w
Scheme i w C. Daje szybkie i małe binarki.

%prep
#%setup -q -n %{name}%{vermain}-%{verminor}
%setup -q -n %{name}%{vermain}
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}/man1 \
	--infodir=%{_infodir} \
	--emacs=/bin/true \
	--jvm=no \
	--cflags="%{rpmcflags}" \
	--coflags="%{rpmcflags}"

%{__make} boot

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for ff in manuals/*.man ; do
	install -p $ff $RPM_BUILD_ROOT%{_mandir}/man1/$(basename $ff .man).1
done

rm -r $RPM_BUILD_ROOT%{_prefix}/doc
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/%{vermain}/Makefile.misc
rm -r $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog manuals/*.html
%dir %{_libdir}/bigloo
%dir %{_libdir}/bigloo/%{vermain}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bigloo/%{vermain}/Makefile.config
%{_libdir}/bigloo/%{vermain}/bigloo.h
%{_libdir}/bigloo/%{vermain}/bigloo_config.*
%{_libdir}/bigloo/%{vermain}/bigloo_gc.h
%{_libdir}/bigloo/%{vermain}/*.init
%{_libdir}/bigloo/%{vermain}/*.*heap
%{_libdir}/bigloo/%{vermain}/lib*.a
%{_libdir}/bigloo/%{vermain}/bmem
%{_libdir}/bigloo/%{vermain}/text
%attr(755,root,root) %{_libdir}/bigloo/%{vermain}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/*
%{_datadir}/info/bigloo.info*
