Summary:	Bigloo is compiler for the Scheme programming language
Summary(pl):	Bigloo - kompilator jêzyka programowania Scheme
Name:		bigloo
Version:	2.6b
Release:	1
License:	see README file
Group:		Development/Languages
Source0:	ftp://ftp-sop.inria.fr/mimosa/fp/Bigloo/%{name}%{version}.tar.gz
# Source0-md5:	bbb788e70fafe2191f1da87c6fdb3f01
Patch0:		%{name}-install.patch
URL:		http://www-sop.inria.fr/mimosa/fp/Bigloo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigloo is a compiler and interpreter for an extended version of the
Scheme programming language. Bigloo allows a full connection between
Scheme and C programs. It delivers fast and small executables.

%description -l pl
Bigloo jest kompilatorem i interpreterem rozszerzonej wersji jêzyka
programowania Scheme. Bigloo pozwala na pe³ne ³±czenie programów w
Scheme i w C. Daje szybkie i ma³e binarki.

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

%{__make} boot

%install
rm -rf $RPM_BUILD_ROOT

BIGLOOLIB=$RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}
export BIGLOOLIB
%{__make} install compile-bee \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-bee \
	DESTDIR=$RPM_BUILD_ROOT
#%{__make} -C fthread install \
#	DESTDIR=$RPM_BUILD_ROOT

install manuals/bigloo.man $RPM_BUILD_ROOT%{_mandir}/man1/bigloo.1
install manuals/afile.man $RPM_BUILD_ROOT%{_mandir}/man1/afile.1
install manuals/jfile.man $RPM_BUILD_ROOT%{_mandir}/man1/jfile.1
install manuals/bdepend.man $RPM_BUILD_ROOT%{_mandir}/man1/bdepend.1
install manuals/bmake.man $RPM_BUILD_ROOT%{_mandir}/man1/bmake.1
install manuals/mco.man $RPM_BUILD_ROOT%{_mandir}/man1/mco.1
install manuals/bpp.man $RPM_BUILD_ROOT%{_mandir}/man1/bpp.1
install manuals/bprof.man $RPM_BUILD_ROOT%{_mandir}/man1/bprof.1
install manuals/btags.man $RPM_BUILD_ROOT%{_mandir}/man1/btags.1

ln -sf %{_libdir}/bigloo/%{version}/libbigloo_s-%{version}.so     $RPM_BUILD_ROOT%{_libdir}/libbigloo_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloo_u-%{version}.so     $RPM_BUILD_ROOT%{_libdir}/libbigloo_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloobdl_s-%{version}.so  $RPM_BUILD_ROOT%{_libdir}/libbigloobdl_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloobdl_u-%{version}.so  $RPM_BUILD_ROOT%{_libdir}/libbigloobdl_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloofth_s-%{version}.so  $RPM_BUILD_ROOT%{_libdir}/libbigloofth_s-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloofth_u-%{version}.so  $RPM_BUILD_ROOT%{_libdir}/libbigloofth_u-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloogc-%{version}.so     $RPM_BUILD_ROOT%{_libdir}/libbigloogc-%{version}.so
ln -sf %{_libdir}/bigloo/%{version}/libbigloogc_fth-%{version}.so $RPM_BUILD_ROOT%{_libdir}/libbigloogc_fth-%{version}.so

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
