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
Version:	4.05
Release:	0.1
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
Patch3:		%{name}-icon.patch
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	bc
BuildRequires:	binutils
#BuildRequires:	control-center-devel
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gle-devel
BuildRequires:	glut-devel
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	esound-devel
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	bc
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xscreensaver-gnome

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
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

%prep
%setup  -q 
install -m755 %{SOURCE4} .

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
#%{__automake}
%{__autoconf}
%configure \
%ifarch alpha
	--without-xshm-ext \
%endif
	--with-xinerama-ext \
	--with-xf86vmode-ext \
	--with-xf86gamma-ext \
	--with-dpms-ext \
	--with-mit-ext \
	--with-proc-interrupts \
	--with-pam \
	--without-motif \
	--with-xml \
	--with-gl \
	--with-gle \
	--with-jpeg \
	--with-xshm-ext \
	--with-xdbe-ext \
	--with-hackdir=%{_prefix}/lib/xscreensaver \
	--with-configdir=%{_sysconfdir}/xscreensaver
#	--with-gtk \
#	--without-gnome \
#	--without-pixbuf \

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pam.d \
	$RPM_BUILD_ROOT{%{_applnkdir}/{Settings/GNOME/Desktop,System},%{_datadir}/control-center/Desktop}

KDEDIR=%{_prefix}; export KDEDIR
%{__make} install install_prefix=$RPM_BUILD_ROOT \
	DESTDIR=$RPM_BUILD_ROOT \
	AD_DIR=%{_libdir}/X11/app-defaults \
	PAM_DIR=/etc/pam.d \
	GNOME_CCDIR=%{_datadir}/control-center/Desktop \
	GNOME_PANELDIR=%{_applnkdir}/Settings/GNOME/Desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/System
%{__make} -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

# Correct desktop files.
correct_desktop()
{
	mv -f "$1" "$1.tmp"
	sed -e "s#$RPM_BUILD_ROOT##" "$1.tmp" > "$1"
	rm -f "$1.tmp"
}

#correct_desktop $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop

#correct_desktop $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop/screensaver-properties.desktop

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

%find_lang %{name} --all-name
cat %{name}.lang >> files.normal

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.normal
%defattr(644,root,root,755)
%doc README README.debugging 
%dir %{_sysconfdir}/%{name}
%doc %{_sysconfdir}/%{name}/README
%config %{_libdir}/X11/app-defaults/*
%{_applnkdir}/System/*
#%{_pixmapsdir}/*.xpm
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%{_mandir}/man1/xscreensaver*
%dir %{_libdir}/xscreensaver
#%attr(755,root,root) %{_bindir}/xscreensaver-demo-gnome
#%attr(755,root,root) %{_bindir}/screensaver-properties-capplet
#%{_applnkdir}/Settings/GNOME/Desktop/*
#%{_datadir}/control-center/Desktop/*
%{_datadir}/%{name}

#%attr(755,root,root) %{_bindir}/xscreensaver.kss


%files GL -f files.gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(644,root,root,755)
