Summary:     X screen savers
Summary(fr): Economiseurs d'�cran X
Summary(pl): Wygaszacz ekranu pod X Window
Name:        xscreensaver
Version:     3.05
Release:     1
Group:       X11/Utilities
Copyright:   BSD
Vendor:      Jamie Zawinski <jwz@netscape.com>
Source0:     %{name}-%{version}.tar.gz
URL:         http://www.jwz.org/xscreensaver
Buildroot:   /tmp/%{name}-%{version}-root

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
monotora to jest te� dost�pny klasyczny "czysty" czarny wygaszacz.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure \
	--prefix=/usr/X11R6 \
	--without-motif
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT/ ; fi
#mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1,lib/X11/app-defaults}
install -d $RPM_BUILD_ROOT/etc/{pam.d,X11/wmconfig}

make install-strip \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	AD_DIR=$RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d

install driver/xscreensaver $RPM_BUILD_ROOT/usr/X11R6/bin
make -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xscreensaver <<EOF
xscreensaver name "xscreensaver (1min timeout)"
xscreensaver description "xscreensaver"
xscreensaver group "Amusements/Screen Savers"
xscreensaver exec "xscreensaver -timeout 1 -cycle 1 &"
EOF

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README README.debugging screenblank.txt
%config /etc/X11/wmconfig/xscreensaver
%config /usr/X11R6/lib/X11/app-defaults/XScreenSaver
/etc/pam.d/xscreensaver
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root, man) /usr/X11R6/man/man1/*

%changelog
* Mon Nov 16 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.04-1]
- added pl translation,
- added using $RPM_OPT_FLAGS during compile,
- based on spec file maked by Fryguy_ <fryguy@falsehope.com>.
