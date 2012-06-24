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
Summary(de.UTF-8):   X-Bildschirmschoner
Summary(es.UTF-8):   Protectores de pantalla X
Summary(fr.UTF-8):   Economiseurs d'écran X
Summary(pl.UTF-8):   Wygaszacze ekranu pod X Window
Summary(pt_BR.UTF-8):   Salvadores de tela X
Summary(ru.UTF-8):   Набор программ хранения экрана для X Window
Summary(uk.UTF-8):   Набір програм збереження екрану для X Window
Summary(zh_CN.UTF-8):   X 窗口系统保护器
Name:		xscreensaver
Version:	4.06
Release:	0.1
Epoch:		1
Group:		X11/Applications
License:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Source4:	mkinstalldirs
Patch1:		%{name}-pofix.patch
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

%description -l de.UTF-8
Dieses Paket enthält eine Sammlung verschiedenster Bildschirmschoner.
Stundenlanger Spaß ist garantiert. Und wenn Sie Ihren Bildschirm
wirklich schonen möchten, gibt's den alten Klassiker, den einfachen
schwarzen Bildschirm.

%description -l es.UTF-8
En este paquete están incluidos protectores de pantalla, de todos los
tipos, garantizando horas de diversión para tu monitor. Y si realmente
estás inclinado a la protección de tu monitor, existe aquel antiguo y
clásico protector, la "pantalla negra".

%description -l fr.UTF-8
Des économiseurs d'écran de chaque sorte sont inclus dans ce paquet,
guarantissant des heures de plaisir et d'économies d'écran. Et si vous
êtes voulez vraiment économiser votre écran, il y a ce vieux
classique, l'écran tout noir.

%description -l pl.UTF-8
Każdy wygaszacz ekranu dołączony do tego pakietu zapewnia godziny
zadowolenia i oszczędzania monitora. Jeśli bardzo Ci zależy na
oszczędzaniu monitora to jest też dostępny klasyczny "czysty" czarny
wygaszacz.

%description -l pt_BR.UTF-8
Protetores de tela de todos os tipos estão incluídos neste pacote,
garantindo horas de divertimento para o seu monitor. E se você
realmente está inclinado à proteção do seu monitor, existe aquele
velho clássico, a "tela preta".

%description -l ru.UTF-8
Пакет xscreensaver содержит разнообразные программы хранения экрана.

%description -l uk.UTF-8
Пакет xscreensaver містить різноманітні програми збереження екрану.

%package GL
Summary:	OpenGL X screen savers
Summary(es.UTF-8):   A set of GL screensavers
Summary(pl.UTF-8):   Wygaszacze ekranu pod X Window używające OpenGL
Summary(pt_BR.UTF-8):   Protetores de tela GL
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	OpenGL

%description GL
Screen savers which uses OpenGL libraries.

%description GL -l es.UTF-8
The xscreensaver-gl package contains even more screensavers for your
mind-numbing, ambition-eroding, time-wasting, hypnotized viewing
pleasure. These screensavers require OpenGL or Mesa support.

%description GL -l pl.UTF-8
Wygaszacze ekranu pod X Window używające OpenGL.

%description GL -l pt_BR.UTF-8
Ainda mais protetores de tela, usando a biblioteca 3D OpenGL.

%package GLE
Summary:	OpenGL && GLE X screen savers
Summary(pl.UTF-8):   Wygaszacze ekranu pod X Window używające OpenGL && GLE
Group:		X11/Applications
Requires:	%{name} = %{version}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl.UTF-8
Wygaszacze ekranu pod X Window używające OpenGL oraz GLE.

%prep
%setup  -q 
%patch1 -p1
install -m755 %{SOURCE4} .

%build
#glib-gettextize --copy --force
#intltoolize --copy --force
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
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

rm -f $RPM_BUILD_ROOT%{_bindir}/screensaver-properties-capplet

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
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%{_mandir}/man1/xscreensaver*
%dir %{_libdir}/xscreensaver
%{_applnkdir}/Settings/GNOME/Desktop/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/%{name}

#%attr(755,root,root) %{_bindir}/xscreensaver.kss


%files GL -f files.gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(644,root,root,755)
