Summary:	Bigloo is compiler for the Scheme programming language
Summary(pl.UTF-8):	Bigloo - kompilator języka programowania Scheme
Name:		bigloo
Version:	3.0b
%define _beta	beta21Aug07
Release:	0.%{_beta}
License:	GPL/LGPL
Group:		Development/Languages
Source0:	ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/%{name}%{version}-%{_beta}.tar.gz
# Source0-md5:	7bee5f27845b018bcc3aaf8795c80294
Patch0:		%{name}-install.patch
URL:		http://www-sop.inria.fr/mimosa/fp/Bigloo/
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
%setup -q -n %{name}%{version}
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

%{__make} -j1 boot

%install
rm -rf $RPM_BUILD_ROOT

BIGLOOLIB=$RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}
export BIGLOOLIB
%{__make} -j1 install compile-bee \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -j1 install-bee \
	DESTDIR=$RPM_BUILD_ROOT
#%{__make} -C fthread install \
#	DESTDIR=$RPM_BUILD_ROOT

install manuals/bigloo.man $RPM_BUILD_ROOT%{_mandir}/man1/bigloo.1
install manuals/bglafile.man $RPM_BUILD_ROOT%{_mandir}/man1/bglafile.1
install manuals/bgljfile.man $RPM_BUILD_ROOT%{_mandir}/man1/bgljfile.1
install manuals/bgldepend.man $RPM_BUILD_ROOT%{_mandir}/man1/bgldepend.1
install manuals/bglmake.man $RPM_BUILD_ROOT%{_mandir}/man1/bglmake.1
install manuals/bglmco.man $RPM_BUILD_ROOT%{_mandir}/man1/bglmco.1
install manuals/bglpp.man $RPM_BUILD_ROOT%{_mandir}/man1/bglpp.1
install manuals/bglprof.man $RPM_BUILD_ROOT%{_mandir}/man1/bglprof.1
install manuals/bgltags.man $RPM_BUILD_ROOT%{_mandir}/man1/bgltags.1

ln -sf %{_libdir}/bigloo/%{version}/libbigloo_s-%{version}.so		$RPM_BUILD_ROOT%{_libdir}/libbigloo_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloo_u-%{version}.so		$RPM_BUILD_ROOT%{_libdir}/libbigloo_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloobdl_s-%{version}.so	$RPM_BUILD_ROOT%{_libdir}/libbigloobdl_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloobdl_u-%{version}.so	$RPM_BUILD_ROOT%{_libdir}/libbigloobdl_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloofth_s-%{version}.so	$RPM_BUILD_ROOT%{_libdir}/libbigloofth_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloofth_u-%{version}.so	$RPM_BUILD_ROOT%{_libdir}/libbigloofth_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloogc-%{version}.so		$RPM_BUILD_ROOT%{_libdir}/libbigloogc-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloogc_fth-%{version}.so	$RPM_BUILD_ROOT%{_libdir}/libbigloogc_fth-%{version}.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog manuals/*.html
%dir %{_libdir}/bigloo
%dir %{_libdir}/bigloo/%{version}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bigloo/%{version}/Makefile.config
%{_libdir}/bigloo/%{version}/bigloo.h
%{_libdir}/bigloo/%{version}/bigloo_config.h
%{_libdir}/bigloo/%{version}/*.init
#%{_libdir}/bigloo/%{version}/*.zip
%{_libdir}/bigloo/%{version}/*.*heap
%{_libdir}/bigloo/%{version}/lib*.a
%{_libdir}/bigloo/%{version}/bmem
%attr(755,root,root) %{_libdir}/bigloo/%{version}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/*
%{_datadir}/info/bigloo.info*
#%%{_datadir}/xemacs/site-lisp/bigloo/*.el*
