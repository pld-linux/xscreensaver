Summary:	X screen savers
Summary(de):	X-Bildschirmschoner
Summary(fr):	Economiseurs d'écran X
Summary(pl):	Wygaszacze ekranu pod X Window
Name:		xscreensaver
Version:	3.23
Release:	1
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Copyright:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
Source1:	xscreensaver.desktop
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	XFree86-devel
BuildRequires:	Mesa-devel >= 3.1
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Screen savers of every sort are included in this package, guaranteeing hours
of enjoyment and monitor saving. And if you are bent on really saving your
monitor, there's that old classic, the plain black screen.

%description -l de
Dieses Paket enthält eine Sammlung verschiedenster Bildschirmschoner. 
Stundenlanger Spaß ist garantiert. Und wenn Sie Ihren Bildschirm wirklich
schonen möchten, gibt's den alten Klassiker, den einfachen schwarzen
Bildschirm.

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
%setup  -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
%ifarch alpha
	--without-xshm-ext" \
%endif
	--without-motif \
	--with-gtk \
	--with-pam \
	--enable-subdir=../lib/xscreensaver

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,usr/X11R6/share/applnk/Utilities}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	AD_DIR=$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d

install driver/xscreensaver $RPM_BUILD_ROOT%{_bindir}
make -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Utilities

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README README.debugging screenblank.txt

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,README.debugging,screenblank.txt}.gz
/usr/X11R6/share/applnk/Utilities/xscreensaver.desktop
%{_libdir}/X11/app-defaults/XScreenSaver
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/xscreensaver

%attr(0755,root,root) %{_bindir}/xscreensaver
%attr(0755,root,root) %{_bindir}/xscreensaver-command
%attr(0755,root,root) %{_bindir}/xscreensaver-demo

%{_mandir}/man1/*

%dir %{_libdir}/xscreensaver
%defattr(755,root,root)
%{_libdir}/xscreensaver/ant
%{_libdir}/xscreensaver/attraction
%{_libdir}/xscreensaver/blaster
%{_libdir}/xscreensaver/blitspin
%{_libdir}/xscreensaver/bouboule
%{_libdir}/xscreensaver/braid
%{_libdir}/xscreensaver/bsod
%{_libdir}/xscreensaver/bubbles
%{_libdir}/xscreensaver/bumps
%{_libdir}/xscreensaver/ccurve
%{_libdir}/xscreensaver/compass
%{_libdir}/xscreensaver/coral
%{_libdir}/xscreensaver/critical
%{_libdir}/xscreensaver/crystal
%{_libdir}/xscreensaver/cynosure
%{_libdir}/xscreensaver/decayscreen
%{_libdir}/xscreensaver/deco
%{_libdir}/xscreensaver/deluxe
%{_libdir}/xscreensaver/demon
%{_libdir}/xscreensaver/discrete
%{_libdir}/xscreensaver/distort
%{_libdir}/xscreensaver/drift
%{_libdir}/xscreensaver/epicycle
%{_libdir}/xscreensaver/fadeplot
%{_libdir}/xscreensaver/flag
%{_libdir}/xscreensaver/flame
%{_libdir}/xscreensaver/flow
%{_libdir}/xscreensaver/forest
%{_libdir}/xscreensaver/galaxy
%{_libdir}/xscreensaver/goop
%{_libdir}/xscreensaver/grav
%{_libdir}/xscreensaver/greynetic
%{_libdir}/xscreensaver/halo
%{_libdir}/xscreensaver/helix
%{_libdir}/xscreensaver/hopalong
%{_libdir}/xscreensaver/hypercube
%{_libdir}/xscreensaver/ifs
%{_libdir}/xscreensaver/imsmap
%{_libdir}/xscreensaver/interference
%{_libdir}/xscreensaver/jigsaw
%{_libdir}/xscreensaver/julia
%{_libdir}/xscreensaver/kaleidescope
%{_libdir}/xscreensaver/kumppa
%{_libdir}/xscreensaver/laser
%{_libdir}/xscreensaver/lightning
%{_libdir}/xscreensaver/lisa
%{_libdir}/xscreensaver/lissie
%{_libdir}/xscreensaver/lmorph
%{_libdir}/xscreensaver/loop
%{_libdir}/xscreensaver/maze
%{_libdir}/xscreensaver/moire
%{_libdir}/xscreensaver/moire2
%{_libdir}/xscreensaver/mountain
%{_libdir}/xscreensaver/munch
%{_libdir}/xscreensaver/noseguy
%{_libdir}/xscreensaver/pedal
%{_libdir}/xscreensaver/penetrate
%{_libdir}/xscreensaver/penrose
%{_libdir}/xscreensaver/petri
%{_libdir}/xscreensaver/phosphor
%{_libdir}/xscreensaver/pyro
%{_libdir}/xscreensaver/qix
%{_libdir}/xscreensaver/rd-bomb
%{_libdir}/xscreensaver/rocks
%{_libdir}/xscreensaver/ripples
%{_libdir}/xscreensaver/rorschach
%{_libdir}/xscreensaver/rotor
%{_libdir}/xscreensaver/sierpinski
%{_libdir}/xscreensaver/shadebobs
%{_libdir}/xscreensaver/slidescreen
%{_libdir}/xscreensaver/slip
%{_libdir}/xscreensaver/sonar
%{_libdir}/xscreensaver/sphere
%{_libdir}/xscreensaver/spiral
%{_libdir}/xscreensaver/spotlight
%{_libdir}/xscreensaver/squiral
%{_libdir}/xscreensaver/starfish
%{_libdir}/xscreensaver/strange
%{_libdir}/xscreensaver/swirl
%{_libdir}/xscreensaver/t3d
%{_libdir}/xscreensaver/triangle
%{_libdir}/xscreensaver/truchet
%{_libdir}/xscreensaver/vidwhacker
%{_libdir}/xscreensaver/vines
%{_libdir}/xscreensaver/wander
%{_libdir}/xscreensaver/webcollage
%{_libdir}/xscreensaver/worm
%{_libdir}/xscreensaver/xflame
%{_libdir}/xscreensaver/xjack
%{_libdir}/xscreensaver/xlyap
%{_libdir}/xscreensaver/xmatrix
%{_libdir}/xscreensaver/xroger
%{_libdir}/xscreensaver/xsublim

%files GL
%defattr(755,root,root)
%{_libdir}/xscreensaver/atlantis
%{_libdir}/xscreensaver/bubble3d
%{_libdir}/xscreensaver/cage
%{_libdir}/xscreensaver/gears
%{_libdir}/xscreensaver/glplanet
%{_libdir}/xscreensaver/lament
%{_libdir}/xscreensaver/moebius
%{_libdir}/xscreensaver/morph3d
%{_libdir}/xscreensaver/pipes
%{_libdir}/xscreensaver/pulsar
%{_libdir}/xscreensaver/rubik
%{_libdir}/xscreensaver/sierpinski3d
%{_libdir}/xscreensaver/sproingies
%{_libdir}/xscreensaver/stairs
%{_libdir}/xscreensaver/superquadrics
