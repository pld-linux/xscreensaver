# TODO:
# make package for KDE with /usr/bin/xscreensaver.kss
#
Summary:	X screen savers
Summary(de.UTF-8):	X-Bildschirmschoner
Summary(es.UTF-8):	Protectores de pantalla X
Summary(fr.UTF-8):	Economiseurs d'écran X
Summary(pl.UTF-8):	Wygaszacze ekranu pod X Window
Summary(pt_BR.UTF-8):	Salvadores de tela X
Summary(ru.UTF-8):	Набор программ хранения экрана для X Window
Summary(uk.UTF-8):	Набір програм збереження екрану для X Window
Summary(zh_CN.UTF-8):	X 窗口系统保护器
Name:		xscreensaver
Version:	5.01
Release:	1
Epoch:		1
License:	BSD
Group:		X11/Applications
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
# Source0-md5:	b60abc52b39591750f48f9c9f20c4167
Source1:	%{name}.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Source4:	mkinstalldirs
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-degnomify.patch
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gle-devel
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	pam-devel >= 0.77.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	%{name}-savers = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3
Requires:	perl-perldoc
Requires:	xorg-lib-libXt >= 1.0.0
Obsoletes:	xscreensaver-gnome
Obsoletes:	xscreensaver-gnome1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_sysconfdir	/etc/X11
%define		_appdefsdir	/usr/share/X11/app-defaults

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

%package common
Summary:	Common X screen savers files
Summary(pl.UTF-8):	Pliki wspólne dla podpakietów wygaszaczy ekranu
Group:		X11/Applications

%description common
Common X screen savers files.

%description common -l pl.UTF-8
Pliki wspólne dla podpakietów wygaszaczy ekranu.

%package base
Summary:	Base X screen savers
Summary(pl.UTF-8):	Podstawowe wygaszacze ekranu pod X Window
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	%{name}-savers = %{epoch}:%{version}-%{release}

%description base
Base screen savers for X Window.

%description base -l pl.UTF-8
Podstawowe wygaszacze ekranu pod X Window.

%package GL
Summary:	OpenGL X screen savers
Summary(pl.UTF-8):	Wygaszacze ekranu pod X Window używające OpenGL
Summary(pt_BR.UTF-8):	Protetores de tela GL
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	%{name}-savers = %{epoch}:%{version}-%{release}

%description GL
Screen savers which uses OpenGL libraries.

%description GL -l pl.UTF-8
Wygaszacze ekranu pod X Window używające OpenGL.

%description GL -l pt_BR.UTF-8
Ainda mais protetores de tela, usando a biblioteca 3D OpenGL.

%package GLE
Summary:	OpenGL & GLE X screen savers
Summary(pl.UTF-8):	Wygaszacze ekranu pod X Window używające OpenGL i GLE
Group:		X11/Applications
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Provides:	%{name}-savers = %{epoch}:%{version}-%{release}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl.UTF-8
Wygaszacze ekranu pod X Window używające OpenGL oraz GLE.

%package gnome2
Summary:	GNOME2 support
Summary(pl.UTF-8):	Wsparcie dla GNOME2
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	control-center >= 1:2.0
Obsoletes:	gnome-screensaver
Obsoletes:	gnome-screensaver-xscreensaver

%description gnome2
GNOME2 support.

%description gnome2 -l pl.UTF-8
Wsparcie dla GNOME2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
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
	AD_DIR=%{_appdefsdir} \
	PAM_DIR=/etc/pam.d

install -d $RPM_BUILD_ROOT{/etc/pam.d,%{_desktopdir}}

install %{SOURCE1} %{SOURCE2} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C driver install-pam \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

_DIR=$(pwd)
cd $RPM_BUILD_ROOT%{_libdir}/%{name}

echo '%defattr(644,root,root,755)' > $_DIR/files.base
echo '%defattr(644,root,root,755)' > $_DIR/files.gl
echo '%defattr(644,root,root,755)' > $_DIR/files.gle

find_config_and_man()
{
	if test -e $RPM_BUILD_ROOT%{_datadir}/%{name}/${1}.xml ; then
		echo %{_datadir}/%{name}/${1}.xml
	fi
	if test -e $RPM_BUILD_ROOT%{_mandir}/man6/${1}.6 ; then
		mv $RPM_BUILD_ROOT%{_mandir}/man6/{,xscreensaver-}${1}.6
		echo %{_mandir}/man6/xscreensaver-${1}.6'*'
		# these two conflict with other packages
		if [ ${1} != barcode -a ${1} != flame ]; then
			echo ".so xscreensaver-${1}.6" > $RPM_BUILD_ROOT%{_mandir}/man6/${1}.6
			echo %{_mandir}/man6/${1}.6'*'
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
		echo "%attr(755,root,root) %{_libdir}/xscreensaver/$file" >> $_DIR/files.gle
		find_config_and_man $file >> $_DIR/files.gle
	elif (echo "$_REQUIRES" | grep -q "libGLU.so"); then
		echo "%attr(755,root,root) %{_libdir}/xscreensaver/$file" >> $_DIR/files.gl
		find_config_and_man $file >> $_DIR/files.gl
	else
		echo "%attr(755,root,root) %{_libdir}/xscreensaver/$file" >> $_DIR/files.base
		find_config_and_man $file >> $_DIR/files.base
	fi
done

cd $_DIR

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.hacking
%doc %{_datadir}/%{name}/README
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%attr(755,root,root) %{_bindir}/xscreensaver-text
#%attr(755,root,root) %{_bindir}/xscreensaver.kss
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xscreensaver
%{_appdefsdir}/*
%{_datadir}/%{name}/glade
%{_desktopdir}/xscreensaver.desktop
%{_desktopdir}/xscreensaver-lock.desktop
%{_mandir}/man1/xscreensaver.1*
%{_mandir}/man1/xscreensaver-command.1*
%{_mandir}/man1/xscreensaver-demo.1*
%{_mandir}/man1/xscreensaver-getimage*.1*
%{_mandir}/man1/xscreensaver-text.1*
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

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper
%{_mandir}/man6/xscreensaver-gl-helper.6*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}

%files base -f files.base
%defattr(644,root,root,755)

%files GL -f files.gl
%defattr(644,root,root,755)

%files GLE -f files.gle
%defattr(644,root,root,755)

%files gnome2
%defattr(644,root,root,755)
%{_desktopdir}/gnome-screensaver-properties.desktop
