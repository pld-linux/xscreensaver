Summary:	X screen savers
Summary(fr):	Economiseurs d'�cran X
Summary(pl):	Wygaszacz ekranu pod X Window
Name:		xscreensaver
Version:	3.12
Release:	1
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Copyright:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
URL:		http://www.jwz.org/xscreensaver/
BuildPrereq:	XFree86-devel
BuildPrereq:	lesstif-devel
BuildPrereq:    xpm-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
Screen savers of every sort are included in this package, guaranteeing hours
of enjoyment and monitor saving. And if you are bent on really saving your
monitor, there's that old classic, the plain black screen.

%description -l fr
Des �conomiseurs d'�cran de chaque sorte sont inclus dans ce paquet,
guarantissant des heures de plaisir et d'�conomies d'�cran. Et si vous �tes
voulez vraiment �conomiser votre �cran, il y a ce vieux classique, l'�cran
tout noir.

%description -l pl
Ka�dy wygaszacz ekranu od��czony do tego pakietu zapewnia godziny
zadowolenia oszcz�dzania monitora. Je�li bardzo Ci zale�y na oszcz�dzaniu
monitora to jest te� dost�pny klasyczny "czysty" czarny wygaszacz.

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--with-motif \
	--with-pam \
	--enable-subdir=../lib/xscreensaver \
	--without-gl

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,X11/wmconfig}

make install-strip \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	AD_DIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d

install driver/xscreensaver $RPM_BUILD_ROOT/usr/X11R6/bin
make -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	README README.debugging screenblank.txt

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xscreensaver <<EOF
xscreensaver name "xscreensaver (1min timeout)"
xscreensaver description "xscreensaver"
xscreensaver group "Amusements/Screen Savers"
xscreensaver exec "xscreensaver -timeout 1 -cycle 1 &"
EOF

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.debugging,screenblank.txt}.gz
/etc/X11/wmconfig/xscreensaver
%config /usr/X11R6/lib/X11/app-defaults/XScreenSaver
%config /etc/pam.d/xscreensaver

%attr(0755,root,root) /usr/X11R6/bin/xscreensaver
%attr(0755,root,root) /usr/X11R6/bin/xscreensaver-command
%attr(0755,root,root) /usr/X11R6/bin/xscreensaver-demo

%dir /usr/X11R6/lib/xscreensaver
%attr(0755,root,root) /usr/X11R6/lib/xscreensaver/*

/usr/X11R6/share/man/man1/*

%changelog
* Mon May 10 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [3.11-1]
- updated to 3.11,
- added Group(pl),
- added BuildPrereq: XFree86-devel,
- removed man group from man pages,
- added gzipping man pages and documetation,
- simplifications in %install,
- moved modules to /usr/X11R6/lib/xscreensaver,
- minor changes,
- recompiled on rpm 3,
- package is now FHS 2.0 compliant.

* Tue Nov 24 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.06-1]
- configure now is runed with --with-motif (we have lesstif).

* Mon Nov 16 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.04-1]
- added pl translation,
- added using $RPM_OPT_FLAGS during compile,
- based on spec file maked by Fryguy_ <fryguy@falsehope.com>.
