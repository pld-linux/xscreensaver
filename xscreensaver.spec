Summary:	X screen savers
Summary(fr):	Economiseurs d'écran X
Summary(pl):	Wygaszacze ekranu pod X Window
Name:		xscreensaver
Version:	3.14
Release:	1
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Copyright:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
URL:		http://www.jwz.org/xscreensaver/
BuildPrereq:	XFree86-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildPrereq:    xpm-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
Screen savers of every sort are included in this package, guaranteeing hours
of enjoyment and monitor saving. And if you are bent on really saving your
monitor, there's that old classic, the plain black screen.

%description -l fr
Des économiseurs d'écran de chaque sorte sont inclus dans ce paquet,
guarantissant des heures de plaisir et d'économies d'écran. Et si vous êtes
voulez vraiment économiser votre écran, il y a ce vieux classique, l'écran
tout noir.

%description -l pl
Ka¿dy wygaszacz ekranu od³±czony do tego pakietu zapewnia godziny
zadowolenia oszczêdzania monitora. Je¶li bardzo Ci zale¿y na oszczêdzaniu
monitora to jest te¿ dostêpny klasyczny "czysty" czarny wygaszacz.

%package GL
Summary:	OpenGL X screen savers
Summary(pl):	Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Requires:	%{name} = %{version}

%description GL
Screen savers which uses OpenGL libraries.

%description -l pl GL
Wygaszacz ekranu pod X Window u¿ywaj±ce OpenGL.

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--without-motif \
	--with-gtk \
	--with-pam \
	--enable-subdir=../lib/xscreensaver

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

/usr/X11R6/share/man/man1/*

%dir /usr/X11R6/lib/xscreensaver
%defattr(755,root,root)
/usr/X11R6/lib/xscreensaver/ant
/usr/X11R6/lib/xscreensaver/attraction
/usr/X11R6/lib/xscreensaver/blitspin
/usr/X11R6/lib/xscreensaver/bouboule
/usr/X11R6/lib/xscreensaver/braid
/usr/X11R6/lib/xscreensaver/bsod
/usr/X11R6/lib/xscreensaver/bubbles
/usr/X11R6/lib/xscreensaver/compass
/usr/X11R6/lib/xscreensaver/coral
/usr/X11R6/lib/xscreensaver/critical
/usr/X11R6/lib/xscreensaver/crystal
/usr/X11R6/lib/xscreensaver/cynosure
/usr/X11R6/lib/xscreensaver/decayscreen
/usr/X11R6/lib/xscreensaver/deco
/usr/X11R6/lib/xscreensaver/deluxe
/usr/X11R6/lib/xscreensaver/demon
/usr/X11R6/lib/xscreensaver/discrete
/usr/X11R6/lib/xscreensaver/distort
/usr/X11R6/lib/xscreensaver/drift
/usr/X11R6/lib/xscreensaver/epicycle
/usr/X11R6/lib/xscreensaver/fadeplot
/usr/X11R6/lib/xscreensaver/flag
/usr/X11R6/lib/xscreensaver/flame
/usr/X11R6/lib/xscreensaver/flow
/usr/X11R6/lib/xscreensaver/forest
/usr/X11R6/lib/xscreensaver/galaxy
/usr/X11R6/lib/xscreensaver/glplanet
/usr/X11R6/lib/xscreensaver/goop
/usr/X11R6/lib/xscreensaver/grav
/usr/X11R6/lib/xscreensaver/greynetic
/usr/X11R6/lib/xscreensaver/halo
/usr/X11R6/lib/xscreensaver/helix
/usr/X11R6/lib/xscreensaver/hopalong
/usr/X11R6/lib/xscreensaver/hypercube
/usr/X11R6/lib/xscreensaver/ifs
/usr/X11R6/lib/xscreensaver/imsmap
/usr/X11R6/lib/xscreensaver/interference
/usr/X11R6/lib/xscreensaver/jigsaw
/usr/X11R6/lib/xscreensaver/julia
/usr/X11R6/lib/xscreensaver/kaleidescope
/usr/X11R6/lib/xscreensaver/kumppa
/usr/X11R6/lib/xscreensaver/laser
/usr/X11R6/lib/xscreensaver/lightning
/usr/X11R6/lib/xscreensaver/lisa
/usr/X11R6/lib/xscreensaver/lissie
/usr/X11R6/lib/xscreensaver/lmorph
/usr/X11R6/lib/xscreensaver/loop
/usr/X11R6/lib/xscreensaver/maze
/usr/X11R6/lib/xscreensaver/moire
/usr/X11R6/lib/xscreensaver/moire2
/usr/X11R6/lib/xscreensaver/mountain
/usr/X11R6/lib/xscreensaver/munch
/usr/X11R6/lib/xscreensaver/noseguy
/usr/X11R6/lib/xscreensaver/pedal
/usr/X11R6/lib/xscreensaver/penetrate
/usr/X11R6/lib/xscreensaver/penrose
/usr/X11R6/lib/xscreensaver/phosphor
/usr/X11R6/lib/xscreensaver/pyro
/usr/X11R6/lib/xscreensaver/qix
/usr/X11R6/lib/xscreensaver/rd-bomb
/usr/X11R6/lib/xscreensaver/rocks
/usr/X11R6/lib/xscreensaver/rorschach
/usr/X11R6/lib/xscreensaver/rotor
/usr/X11R6/lib/xscreensaver/sierpinski
/usr/X11R6/lib/xscreensaver/slidescreen
/usr/X11R6/lib/xscreensaver/slip
/usr/X11R6/lib/xscreensaver/sonar
/usr/X11R6/lib/xscreensaver/sphere
/usr/X11R6/lib/xscreensaver/spiral
/usr/X11R6/lib/xscreensaver/spotlight
/usr/X11R6/lib/xscreensaver/squiral
/usr/X11R6/lib/xscreensaver/starfish
/usr/X11R6/lib/xscreensaver/strange
/usr/X11R6/lib/xscreensaver/swirl
/usr/X11R6/lib/xscreensaver/t3d
/usr/X11R6/lib/xscreensaver/triangle
/usr/X11R6/lib/xscreensaver/truchet
/usr/X11R6/lib/xscreensaver/vines
/usr/X11R6/lib/xscreensaver/wander
/usr/X11R6/lib/xscreensaver/worm
/usr/X11R6/lib/xscreensaver/xflame
/usr/X11R6/lib/xscreensaver/xjack
/usr/X11R6/lib/xscreensaver/xlyap
/usr/X11R6/lib/xscreensaver/xmatrix
/usr/X11R6/lib/xscreensaver/xroger

%files GL
%defattr(755,root,root)
/usr/X11R6/lib/xscreensaver/atlantis
/usr/X11R6/lib/xscreensaver/bubble3d
/usr/X11R6/lib/xscreensaver/cage
/usr/X11R6/lib/xscreensaver/gears
/usr/X11R6/lib/xscreensaver/lament
/usr/X11R6/lib/xscreensaver/moebius
/usr/X11R6/lib/xscreensaver/morph3d
/usr/X11R6/lib/xscreensaver/pipes
/usr/X11R6/lib/xscreensaver/pulsar
/usr/X11R6/lib/xscreensaver/rubik
/usr/X11R6/lib/xscreensaver/sproingies
/usr/X11R6/lib/xscreensaver/stairs
/usr/X11R6/lib/xscreensaver/superquadrics

%changelog
* Fri May 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.11-2]
- added GL subpackage with screen savers which uses OpenGL libraries.

* Mon May 10 1999 Piotr Czerwiñski <pius@pld.org.pl>
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

* Tue Nov 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.06-1]
- configure now is runed with --with-motif (we have lesstif).

* Mon Nov 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.04-1]
- added pl translation,
- added using $RPM_OPT_FLAGS during compile,
- based on spec file maked by Fryguy_ <fryguy@falsehope.com>.
