# TODO:
# make package for KDE with /usr/X11R6/bin/xscreensaver.kss
#
# Conditional build:
#%%bcond_with gnome1		# build package with gnome1 support
#
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
Version:	4.21
Release:	0.1
Epoch:		1
Group:		X11/Applications
License:	BSD
Source0:	http://www.jwz.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3ea7d0bc9b7159523855296e175d7ac7
Source1:	%{name}.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Source4:	mkinstalldirs
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-fix-launch-with-kde.patch
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gle-devel
BuildRequires:	glut-devel
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	pam-devel >= 0.77.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	pam >= 0.77.3
Requires:	perl-perldoc
Obsoletes:	xscreensaver-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_sysconfdir	/etc/X11
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl
Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL oraz GLE.

%package gnome2
Summary:	GNOME2 support
Summary(pl):	Wsparcie dla GNOME2
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	control-center >= 1:2.0

%description gnome2
GNOME2 support.

%description gnome2 -l pl
Wsparcie dla GNOME2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%%patch2 -p1
install -m755 %{SOURCE4} .

mv po/{no,nb}.po

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	PERL=%{__perl} \
%ifarch alpha
	--without-xshm-ext \
%endif
	--with-xinerama-ext \
	--with-randr-ext \
	--with-xf86vmode-ext \
	--with-xf86gamma-ext \
	--with-dpms-ext \
	--with-mit-ext \
	--with-proc-interrupts \
	--with-pam \
	--with-shadow \
	--without-motif \
	--with-xml \
	--with-gl \
	--with-gle \
	--with-jpeg \
	--with-xshm-ext \
	--with-xdbe-ext \
	--with-hackdir=%{_libdir}/xscreensaver \
	--with-configdir=%{_datadir}/xscreensaver \
	--with-fortune=%{_bindir}/fortune \
	--enable-locking

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_prefix=$RPM_BUILD_ROOT \
	PAM_DIR=/etc/pam.d \
	GNOME_CCDIR_1=%{_datadir}/control-center/Desktop \
	GNOME_CCDIR_2=%{_datadir}/control-center/capplets \
	GNOME_PANELDIR=%{_applnkdir}/Settings/GNOME/Desktop

install -d $RPM_BUILD_ROOT{/etc/pam.d,%{_desktopdir}}

install %{SOURCE1} %{SOURCE2} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C driver install-pam \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

_DIR=$(pwd)
cd $RPM_BUILD_ROOT%{_libdir}/%{name}

echo '%defattr(755,root,root)' > $_DIR/files.normal
echo '%defattr(755,root,root)' > $_DIR/files.gl
echo '%defattr(755,root,root)' > $_DIR/files.gle

find_config_and_man()
{
	if test -e $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/${1}.xml ; then
		echo %{_sysconfdir}/%{name}/${1}.xml
	fi
	if test -e $RPM_BUILD_ROOT%{_mandir}/man1/${1}.1 ; then
		mv $RPM_BUILD_ROOT%{_mandir}/man1/{,xscreensaver-}${1}.1
		echo %{_mandir}/man1/xscreensaver-${1}.1'*'
		# these two conflict with other packages
		if [ ${1} != barcode -a ${1} != flame ]; then
			echo ".so xscreensaver-${1}.1" > $RPM_BUILD_ROOT%{_mandir}/man1/${1}.1
			echo %{_mandir}/man1/${1}.1'*'
		fi
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

%find_lang %{name} --all-name
cat %{name}.lang >> files.normal

install -d $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.normal
%defattr(644,root,root,755)
%doc README README.debugging
%doc %{_datadir}/%{name}/README
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%attr(755,root,root) %{_bindir}/xscreensaver-text
#%attr(755,root,root) %{_bindir}/xscreensaver.kss
#%dir %{_datadir}/%{name}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/xscreensaver
%dir %{_libdir}/xscreensaver
%{_appdefsdir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/xscreensaver*
%{_pixmapsdir}/*.xpm

#%{_datadir}/%{name}/cosmos.xml
#%{_datadir}/%{name}/electricsheep.xml
#%{_datadir}/%{name}/fireflies.xml
#%{_datadir}/%{name}/goban.xml
#%{_datadir}/%{name}/sphereeversion.xml
#%{_datadir}/%{name}/ssystem.xml
#%{_datadir}/%{name}/xaos.xml
#%{_datadir}/%{name}/xdaliclock.xml
#%{_datadir}/%{name}/xearth.xml
#%{_datadir}/%{name}/xfishtank.xml
#%{_datadir}/%{name}/xmountains.xml
#%{_datadir}/%{name}/xplanet.xml
#%{_datadir}/%{name}/xsnow.xml

%files GL -f files.gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(644,root,root,755)

%files gnome2
%defattr(644,root,root,755)
%{_desktopdir}/gnome-screensaver-properties.desktop
