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
Summary(fr):	Economiseurs d'Ècran X
Summary(pl):	Wygaszacze ekranu pod X Window
Summary(pt_BR):	Salvadores de tela X
Summary(ru):	Ó¡¬œ“ –“œ«“¡ÕÕ »“¡Œ≈Œ…— ‹À“¡Œ¡ ƒÃ— X Window
Summary(uk):	Ó¡¬¶“ –“œ«“¡Õ ⁄¬≈“≈÷≈ŒŒ— ≈À“¡Œ’ ƒÃ— X Window
Summary(zh_CN):	X ¥∞ø⁄œµÕ≥±£ª§∆˜
Name:		xscreensaver
Version:	4.13
Release:	1
Epoch:		1
Group:		X11/Applications
License:	BSD
Source0:	http://www.jwz.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	48fa73157e58801672f40ead4a673e91
Source1:	%{name}.desktop
Source2:	%{name}-lock.desktop
Source3:	%{name}.pamd
Source4:	mkinstalldirs
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	bc
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gle-devel
BuildRequires:	glut-devel
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	pam-devel
BuildRequires:	perl-base
Requires:	pam >= 0.77.3
Obsoletes:	xscreensaver-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_sysconfdir	/etc/X11
%define		_xprefix	/usr/X11R6

%description
Screen savers of every sort are included in this package, guaranteeing
hours of enjoyment and monitor saving. And if you are bent on really
saving your monitor, there's that old classic, the plain black screen.

%description -l de
Dieses Paket enth‰lt eine Sammlung verschiedenster Bildschirmschoner.
Stundenlanger Spaﬂ ist garantiert. Und wenn Sie Ihren Bildschirm
wirklich schonen mˆchten, gibt's den alten Klassiker, den einfachen
schwarzen Bildschirm.

%description -l es
En este paquete est·n incluidos protectores de pantalla, de todos los
tipos, garantizando horas de diversiÛn para tu monitor. Y si realmente
est·s inclinado a la protecciÛn de tu monitor, existe aquel antiguo y
cl·sico protector, la "pantalla negra".

%description -l fr
Des Èconomiseurs d'Ècran de chaque sorte sont inclus dans ce paquet,
guarantissant des heures de plaisir et d'Èconomies d'Ècran. Et si vous
Ítes voulez vraiment Èconomiser votre Ècran, il y a ce vieux
classique, l'Ècran tout noir.

%description -l pl
Kaødy wygaszacz ekranu do≥±czony do tego pakietu zapewnia godziny
zadowolenia i oszczÍdzania monitora. Je∂li bardzo Ci zaleøy na
oszczÍdzaniu monitora to jest teø dostÍpny klasyczny "czysty" czarny
wygaszacz.

%description -l pt_BR
Protetores de tela de todos os tipos est„o incluÌdos neste pacote,
garantindo horas de divertimento para o seu monitor. E se vocÍ
realmente est· inclinado ‡ proteÁ„o do seu monitor, existe aquele
velho cl·ssico, a "tela preta".

%description -l ru
¡À≈‘ xscreensaver ”œƒ≈“÷…‘ “¡⁄Œœœ¬“¡⁄ŒŸ≈ –“œ«“¡ÕÕŸ »“¡Œ≈Œ…— ‹À“¡Œ¡.

%description -l uk
¡À≈‘ xscreensaver Õ¶”‘…‘ÿ “¶⁄ŒœÕ¡Œ¶‘Œ¶ –“œ«“¡Õ… ⁄¬≈“≈÷≈ŒŒ— ≈À“¡Œ’.

%package GL
Summary:	OpenGL X screen savers
Summary(es):	A set of GL screensavers
Summary(pl):	Wygaszacze ekranu pod X Window uøywaj±ce OpenGL
Summary(pt_BR):	Protetores de tela GL
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	OpenGL

%description GL
Screen savers which uses OpenGL libraries.

%description GL -l es
The xscreensaver-gl package contains even more screensavers for your
mind-numbing, ambition-eroding, time-wasting, hypnotized viewing
pleasure. These screensavers require OpenGL or Mesa support.

%description GL -l pl
Wygaszacze ekranu pod X Window uøywaj±ce OpenGL.

%description GL -l pt_BR
Ainda mais protetores de tela, usando a biblioteca 3D OpenGL.

%package GLE
Summary:	OpenGL && GLE X screen savers
Summary(pl):	Wygaszacze ekranu pod X Window uøywaj±ce OpenGL && GLE
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description GLE -l pl
Wygaszacze ekranu pod X Window uøywaj±ce OpenGL oraz GLE.

%package gnome1
Summary:	GNOME1 support
Summary(pl):	Wsparcie dla GNOME1
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	control-center < 2.0

%description gnome1
GNOME1 support.

%description gnome1 -l pl
Wsparcie dla GNOME1.

%package gnome2
Summary:	GNOME2 support
Summary(pl):	Wsparcie dla GNOME2
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	control-center >= 2.0

%description gnome2
GNOME2 support.

%description gnome2 -l pl
Wsparcie dla GNOME2.

%prep
%setup -q
install -m755 %{SOURCE4} .

%build
%configure \
	PERL=%{__perl} \
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
	--with-configdir=%{_sysconfdir}/xscreensaver \
	--with-fortune=%{_bindir}/fortune

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_prefix=$RPM_BUILD_ROOT \
	PAM_DIR=/etc/pam.d \
	GNOME_CCDIR_1=%{_xprefix}/share/control-center/Desktop \
	GNOME_CCDIR_2=%{_xprefix}/share/control-center/capplets \
	GNOME_PANELDIR=%{_applnkdir}/Settings/GNOME/Desktop

install -d $RPM_BUILD_ROOT{/etc/pam.d,%{_applnkdir}/Settings/Xscreensaver}

install %{SOURCE1} %{SOURCE2} \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Xscreensaver

%{__make} -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

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
%doc %{_sysconfdir}/%{name}/README
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
#%attr(755,root,root) %{_bindir}/xscreensaver.kss
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/xscreensaver
%dir %{_libdir}/xscreensaver
%{_xprefix}/lib/X11/app-defaults/*
%{_datadir}/%{name}
%{_applnkdir}/Settings/Xscreensaver
%{_mandir}/man1/xscreensaver*
%{_pixmapsdir}/*.xpm

%files GL -f files.gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(644,root,root,755)

%files gnome1
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/screensaver-properties-capplet
%{_xprefix}/share/control-center/Desktop/*
%{_xprefix}/share/control-center/capplets/*
%{_applnkdir}/Settings/GNOME/Desktop/*

%files gnome2
%defattr(644,root,root,755)
%{_datadir}/control-center-2.0/capplets/*
