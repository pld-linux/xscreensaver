# TODO:
# make packages with additionals hacks:
# - cosmos
# - electricsheep
# - goban
# - sphereEversion
# - ssystem
# - xaos
# - xdaliclock
# - xearth
# - xfishtank
# - xmountains
# - xsnow (partialy done)
# make package for KDE with /usr/X11R6/bin/xscreensaver.kss
Summary:	X screen savers
Summary(de):	X-Bildschirmschoner
Summary(es):	Protectores de pantalla X
Summary(fr):	Economiseurs d'écran X
Summary(pl):	Wygaszacze ekranu pod X Window
Summary(pt_BR):	Salvadores de tela X
Summary(ru):	îÁÂÏÒ ÐÒÏÇÒÁÍÍ ÈÒÁÎÅÎÉÑ ÜËÒÁÎÁ ÄÌÑ X Window
Summary(uk):	îÁÂ¦Ò ÐÒÏÇÒÁÍ ÚÂÅÒÅÖÅÎÎÑ ÅËÒÁÎÕ ÄÌÑ X Window
Summary(zh_CN):	X ´°¿ÚÏµÍ³±£»¤Æ÷
Name:		xscreensaver
Version:	4.03
Release:	1
Epoch:		1
Group:		X11/Applications
License:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Source4:	mkinstalldirs
Patch1:		%{name}-c++.patch
Patch2:		%{name}-xml.patch
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	gle-devel
BuildRequires:	glut-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	control-center-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel
BuildRequires:	bc
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	grep
BuildRequires:	awk
BuildRequires:	binutils
BuildRequires:	autoconf >= 2.53
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
Screen savers of every sort are included in this package, guaranteeing
hours of enjoyment and monitor saving. And if you are bent on really
saving your monitor, there's that old classic, the plain black screen.

%description -l de
Dieses Paket enthält eine Sammlung verschiedenster Bildschirmschoner.
Stundenlanger Spaß ist garantiert. Und wenn Sie Ihren Bildschirm
wirklich schonen möchten, gibt's den alten Klassiker, den einfachen
schwarzen Bildschirm.

%description -l es
En este paquete están incluidos protectores de pantalla, de todos los
tipos, garantizando horas de diversión para tu monitor. Y si realmente
estás inclinado a la protección de tu monitor, existe aquel antiguo y
clásico protector, la "pantalla negra".

%description -l fr
Des économiseurs d'écran de chaque sorte sont inclus dans ce paquet,
guarantissant des heures de plaisir et d'économies d'écran. Et si vous
êtes voulez vraiment économiser votre écran, il y a ce vieux
classique, l'écran tout noir.

%description -l pl
Ka¿dy wygaszacz ekranu do³±czony do tego pakietu zapewnia godziny
zadowolenia i oszczêdzania monitora. Je¶li bardzo Ci zale¿y na
oszczêdzaniu monitora to jest te¿ dostêpny klasyczny "czysty" czarny
wygaszacz.

%description -l pt_BR
Protetores de tela de todos os tipos estão incluídos neste pacote,
garantindo horas de divertimento para o seu monitor. E se você
realmente está inclinado à proteção do seu monitor, existe aquele
velho clássico, a "tela preta".

%description -l ru
ðÁËÅÔ xscreensaver ÓÏÄÅÒÖÉÔ ÒÁÚÎÏÏÂÒÁÚÎÙÅ ÐÒÏÇÒÁÍÍÙ ÈÒÁÎÅÎÉÑ ÜËÒÁÎÁ.

%description -l uk
ðÁËÅÔ xscreensaver Í¦ÓÔÉÔØ Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ÐÒÏÇÒÁÍÉ ÚÂÅÒÅÖÅÎÎÑ ÅËÒÁÎÕ.

%package GL
Summary:	OpenGL X screen savers
Summary(es):	A set of GL screensavers
Summary(pl):	Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL
Summary(pt_BR):	Protetores de tela GL
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	OpenGL

%description GL
Screen savers which uses OpenGL libraries.

%description GL -l es
The xscreensaver-gl package contains even more screensavers for your
mind-numbing, ambition-eroding, time-wasting, hypnotized viewing
pleasure. These screensavers require OpenGL or Mesa support.

%description GL -l pl
Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL.

%description GL -l pt_BR
Ainda mais protetores de tela, usando a biblioteca 3D OpenGL.

%package GLE
Summary:	OpenGL && GLE X screen savers
Summary(pl):	Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL && GLE
Group:		X11/Applications
Requires:	%{name} = %{version}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl
Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL oraz GLE.

%package gnome
Summary:	xscreensaver - GNOME support files
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gnome
.

%prep
%setup  -q
%patch1 -p1
%patch2 -p1
install -m755 %{SOURCE4} mkinstalldirs

%build
gettextize --copy --force
sed 's/@PACKAGE@/@GETTEXT_PACKAGE@/' po/Makefile.in.in >po/Makefile.in.in.fixed
mv po/Makefile.in.in.fixed po/Makefile.in.in
aclocal
autoconf
# Build GNOME-free version.
%configure \
%ifarch alpha
	--without-xshm-ext \
%endif
	--without-motif \
	--with-gtk \
	--with-xml \
	--without-gnome \
	--without-pixbuf \
	--with-jpeg \
	--with-pam \
	--with-dpms-ext \
	--with-xdbe-ext \
	--with-mit-ext \
	--with-xinerama-ext \
	--with-xf86vmode-ext \
	--with-xf86gamma-ext \
	--with-proc-interrupts \
	--with-gl \
	--with-gle \
	--with-hackdir=%{_prefix}/lib/xscreensaver \
	--with-configdir=%{_sysconfdir}/xscreensaver

%{__make} all

mv -f driver/xscreensaver-demo{,-gnomefree}

# Build GNOME version.
# This version has to be build last in order for "make install" to install
# desktop files.
rm -f config.cache driver/xscreensaver-demo{,-Gtk} `find driver -name '*.o'`

%configure \
%ifarch alpha
	--without-xshm-ext \
%endif
	--without-motif \
	--with-gtk \
	--with-xml \
	--with-gnome \
	--with-pixbuf \
	--with-jpeg \
	--with-pam \
	--with-dpms-ext \
	--with-xdbe-ext \
	--with-mit-ext \
	--with-xinerama-ext \
	--with-xf86vmode-ext \
	--with-xf86gamma-ext \
	--with-proc-interrupts \
	--with-gl \
	--with-gle \
	--with-hackdir=%{_prefix}/lib/xscreensaver \
	--with-configdir=%{_sysconfdir}/xscreensaver

cd driver
%{__make} xscreensaver-demo
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pam.d \
	$RPM_BUILD_ROOT{%{_applnkdir}/{Settings/GNOME/Desktop,System},%{_datadir}/control-center/Desktop}

export KDEDIR=%{_prefix}
%{__make} install install_prefix=$RPM_BUILD_ROOT \
	DESTDIR=$RPM_BUILD_ROOT \
	AD_DIR=%{_libdir}/X11/app-defaults \
	PAM_DIR=/etc/pam.d \
	GNOME_CCDIR=%{_datadir}/control-center/Desktop \
	GNOME_PANELDIR=%{_applnkdir}/Settings/GNOME/Desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/System
install driver/xscreensaver $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_bindir}/xscreensaver-demo{,-gnome}
install driver/xscreensaver-demo-gnomefree $RPM_BUILD_ROOT%{_bindir}/xscreensaver-demo
%{__make} -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

gzip -9nf README README.debugging screenblank.txt

# Correct desktop files.
correct_desktop()
{
	mv -f "$1" "$1.tmp"
	sed -e "s#$RPM_BUILD_ROOT##" -e s/xscreensaver-demo/xscreensaver-demo-gnome/ "$1.tmp" > "$1"
	rm -f "$1.tmp"
}

correct_desktop $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop

correct_desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop/screensaver-properties.desktop

_DIR=$(pwd)
cd $RPM_BUILD_ROOT%{_libdir}/%{name}

echo '%defattr(755,root,root)' > $_DIR/files.normal
echo '%defattr(755,root,root)' > $_DIR/files.gl
echo '%defattr(755,root,root)' > $_DIR/files.gle

find_config_and_man()
{
	if test -e $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/${1}.xml ; then
		echo %{_sysconfdir}/%{name}/${1}.xml
	fi
	if test -e $RPM_BUILD_ROOT/%{_mandir}/man1/${1}.1 ; then
		echo %{_mandir}/man1/${1}.1'*'
	fi
}

for file in * ; do
	_REQUIRES="`objdump -p $file 2> /dev/null | awk '
		BEGIN { START=0; LIBNAME=""; }
		/Dynamic Section:/ { START=1; }
		/NEEDED/ && (START==1) {
			LIBNAME=$2;
		}
		(START==1) && (LIBNAME!="") { print LIBNAME; }
		/^$/ { START=0; }' 2>&1 `"

if (echo "$_REQUIRES" | grep -q "libgle.so"); then
	echo "%{_libdir}/xscreensaver/$file" >> $_DIR/files.gle
	find_config_and_man $file >> $_DIR/files.gle
elif (echo "$_REQUIRES" | grep -q "libGLU.so"); then
	echo "%{_libdir}/xscreensaver/$file" >> $_DIR/files.gl
	find_config_and_man $file >> $_DIR/files.gl
else
	echo "%{_libdir}/xscreensaver/$file" >> $_DIR/files.normal
	find_config_and_man $file >> $_DIR/files.normal
fi
done

cd $_DIR

%find_lang %{name}
cat %{name}.lang >> files.normal

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.normal
%defattr(644,root,root,755)
%doc {README,README.debugging,screenblank.txt}.gz
%dir %{_sysconfdir}/%{name}
%doc %{_sysconfdir}/%{name}/README
%config %{_libdir}/X11/app-defaults/*
%{_applnkdir}/System/*
%{_pixmapsdir}/*.xpm
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%{_mandir}/man1/xscreensaver*
%dir %{_libdir}/xscreensaver

%files GL -f files.gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(644,root,root,755)

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-demo-gnome
%attr(755,root,root) %{_bindir}/screensaver-properties-capplet
%{_applnkdir}/Settings/GNOME/Desktop/*
%{_datadir}/control-center/Desktop/*

#%attr(755,root,root) %{_bindir}/xscreensaver.kss
