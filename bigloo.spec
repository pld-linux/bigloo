%define		vermain		4.7a
#define		verminor	5
Summary:	Bigloo is compiler for the Scheme programming language
Summary(pl.UTF-8):	Bigloo - kompilator języka programowania Scheme
Name:		bigloo
#Version:	%{vermain}.%{verminor}
Version:	%{vermain}
Release:	1
License:	GPL/LGPL
Group:		Development/Languages
#Source0:	https://www-sop.inria.fr/indes/fp/Bigloo/download/%{name}-%{vermain}-%{verminor}.tar.gz
Source0:	https://www-sop.inria.fr/indes/fp/Bigloo/download/%{name}-%{vermain}.tar.gz
# Source0-md5:	8712ededcf19110781c6dc214b878803
Patch0:		%{name}-install.patch
URL:		https://www-sop.inria.fr/indes/fp/Bigloo/
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
%setup -q -n %{name}-%{vermain}
%patch -P0 -p1

%build
# bigloo 4.6a runtime uses K&R-style function pointer declarations
# (e.g. void (*f)()) that C23 rejects; pin gnu17 across compiler probes too.
CC="%{__cc} -std=gnu17" \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}/man1 \
	--infodir=%{_infodir} \
	--emacs=/bin/true \
	--jvm=no \
	--cflags="-std=gnu17 %{rpmcppflags} %{rpmcflags}" \
	--coflags="-std=gnu17 %{rpmcppflags} %{rpmcflags}" \
	--ldflags="%{rpmldflags}"

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
%doc README.md ChangeLog manuals/*.html
%attr(755,root,root) %{_bindir}/bgl*
%attr(755,root,root) %{_bindir}/bigloo
%attr(755,root,root) %{_bindir}/bigloo.sh
%attr(755,root,root) %{_bindir}/bigloo%{vermain}
%dir %{_libdir}/bigloo
%{_libdir}/bigloo/%{vermain}
%{_mandir}/man1/*
%{_infodir}/bigloo.info*
