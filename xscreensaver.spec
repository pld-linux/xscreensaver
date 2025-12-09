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
Version:	6.13
Release:	1
Epoch:		1
License:	BSD
Group:		X11/Applications
Source0:	https://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
# Source0-md5:	b30f5738bd5aab0e50fce337d28a487e
Source1:	%{name}-autostart.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Patch0:		%{name}-desktop.patch
URL:		https://www.jwz.org/xscreensaver/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel >= 1.3
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bc
BuildRequires:	gdk-pixbuf2-xlib-devel >= 2.0.0
BuildRequires:	gettext-tools
BuildRequires:	gle-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.22.0
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	pam-devel >= 0.77.3
BuildRequires:	perl-base
BuildRequires:	perl-perldoc
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	systemd-devel >= 1:221
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1.0
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	%{name}-savers = %{epoch}:%{version}-%{release}
Requires:	gtk+2 >= 1:2.22.0
Requires:	pam >= 0.77.3
Requires:	xdg-utils
Requires:	xorg-lib-libXt >= 1.0.0
# for screensaver-getimage-file
Suggests:	perl-perldoc
# for xscreensaver-text
Suggests:	xorg-app-appres
Obsoletes:	xscreensaver-gnome < 1:4.06
Obsoletes:	xscreensaver-gnome1 < 1:4.21
Obsoletes:	xscreensaver-gnome2 < 1:5.06
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	perl-HTML-Parser
Requires:	perl-LWP-Protocol-https
Requires:	xorg-lib-libXft >= 2.1.0
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
Requires:	xorg-lib-libXft >= 2.1.0
Provides:	%{name}-savers = %{epoch}:%{version}-%{release}
# for starwars req: xscreensaver-text
Suggests:	%{name}

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
Requires:	xorg-lib-libXft >= 2.1.0
Provides:	%{name}-savers = %{epoch}:%{version}-%{release}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl.UTF-8
Wygaszacze ekranu pod X Window używające OpenGL oraz GLE.

%prep
%setup -q -n %{name}-%{version}
%patch -P 0 -p1

# fix encoding (xscreensaver-6.05: actual encoding is ISO-8869-1, but file specifies UTF-8)
iconv -f iso-8859-1 -t utf-8 po/ca.po -o po/ca.po.tmp
%{__mv} po/ca.po.tmp po/ca.po

# from Fedora:
# xscreensaver 6.03: manually fix po/Makefile.in.in
cd po
sed -i Makefile.in.in \
	-e "\@^POFILES[ \t]*=@s@^.*@POTFILES\t=$(ls -1 *po | while read f ; do echo -n -e " $f" ; done)@" \
	-e "\@^GMOFILES[ \t]*=@s@^.*@GMOTFILES\t=$(ls -1 *po | while read f ; do echo -n -e " ${f%.po}.gmo" ; done)@" \
	-e "\@^CATALOGS[ \t]*=@s@^.*@CATALOGS\t=$(ls -1 *po | while read f ; do echo -n -e " ${f%.po}.gmo" ; done)@" \
	-e "\@^CATOBJEXT[ \t]*=@s@^.*@CATOBJEXT\t= .gmo@" \
	-e "\@^INSTOBJEXT[ \t]*=@s@^.*@INSTOBJEXT\t= .mo@" \
	-e "\@^MKINSTALLDIRS[ \t]*=@s@^.*@MKINSTALLDIRS\t= install -d@" \
        %{nil}
cd -

# fix shebangs
%{__sed} -i '1s,/usr/bin/env xdg-open$,/usr/bin/xdg-open,' \
		driver/{xscreensaver-settings.desktop.in,xscreensaver.desktop.in}

%build
%configure \
	--with-x \
	--with-dpms-ext \
	--with-xf86vmode-ext \
	--with-xinerama-ext \
	--with-randr-ext \
	--with-xinput-ext \
	--with-xf86gamma-ext \
	--with-xshm-ext \
	--with-xdbe-ext \
	--with-xkb-ext \
	--with-proc-interrupts \
	--with-proc-oom \
	--with-systemd \
	--with-pam \
	--with-shadow \
	--with-gtk \
	--with-gl \
	--with-gle \
	--with-jpeg \
	--with-png \
	--with-pixbuf \
	--with-xft \
	--with-hackdir=%{_libdir}/xscreensaver \
	--with-configdir=%{_datadir}/xscreensaver \
	--enable-locking \
	--without-login-manager \
	--without-kerberos \
	--without-motif

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_sh=$(pwd)/install-sh \
	install_prefix=$RPM_BUILD_ROOT \
	AD_DIR=%{_appdefsdir} \
	PAM_DIR=/etc/pam.d

install -d $RPM_BUILD_ROOT{/etc/{pam.d,xdg/autostart},%{_desktopdir}}

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/xdg/autostart
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C driver install-pam \
	PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

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
		%{__mv} $RPM_BUILD_ROOT%{_mandir}/man6/{,xscreensaver-}${1}.6
		echo %{_mandir}/man6/xscreensaver-${1}.6'*'
		# these two conflict with other packages
		if [ ${1} != barcode -a ${1} != flame ]; then
			echo ".so xscreensaver-${1}.6" > $RPM_BUILD_ROOT%{_mandir}/man6/${1}.6
			echo %{_mandir}/man6/${1}.6'*'
		fi
	fi
}

for file in *; do
	_REQUIRES=$(objdump -p $file 2> /dev/null | awk '
		BEGIN { START=0; LIBNAME=""; }
		/Dynamic Section:/ { START=1; }
		/NEEDED/ && (START==1) {
			LIBNAME=$2;
		}
		(START==1) && (LIBNAME!="") { print LIBNAME; }
		/^$/ { START=0; }')

	if echo "$_REQUIRES" | grep -q "libgle.so"; then
		echo "%attr(755,root,root) %{_libdir}/xscreensaver/$file" >> $_DIR/files.gle
		find_config_and_man $file >> $_DIR/files.gle
	elif echo "$_REQUIRES" | grep -q "libGLU.so"; then
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

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.hacking
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-settings
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/README
%{_datadir}/%{name}/xscreensaver.service
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xscreensaver
/etc/xdg/autostart/xscreensaver-autostart.desktop
%{_appdefsdir}/XScreenSaver
%{_mandir}/man1/xscreensaver.1*
%{_mandir}/man1/xscreensaver-command.1*
%{_mandir}/man1/xscreensaver-demo.1*
%{_mandir}/man1/xscreensaver-settings.1*
%{_desktopdir}/xscreensaver-lock.desktop
%{_desktopdir}/xscreensaver-settings.desktop
%{_desktopdir}/xscreensaver.desktop
%{_pixmapsdir}/xscreensaver.png

%files common
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_fontsdir}/xscreensaver
%{_fontsdir}/xscreensaver/*.ttf

%files base -f files.base
%defattr(644,root,root,755)

%files GL -f files.gl
%defattr(644,root,root,755)

%files GLE -f files.gle
%defattr(644,root,root,755)
