Summary:	X screen savers
Summary(de):	X-Bildschirmschoner
Summary(fr):	Economiseurs d'écran X
Summary(pl):	Wygaszacze ekranu pod X Window
Name:		xscreensaver
Version:	3.33
Release:	1
Epoch:		1
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
License:	BSD
Source0:	http://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.pamd
URL:		http://www.jwz.org/xscreensaver/
BuildRequires:	OpenGL-devel
BuildRequires:	gle-devel
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xscreensaver-gnome

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Screen savers of every sort are included in this package, guaranteeing
hours of enjoyment and monitor saving. And if you are bent on really
saving your monitor, there's that old classic, the plain black screen.

%description -l de
Dieses Paket enthält eine Sammlung verschiedenster Bildschirmschoner.
Stundenlanger Spaß ist garantiert. Und wenn Sie Ihren Bildschirm
wirklich schonen möchten, gibt's den alten Klassiker, den einfachen
schwarzen Bildschirm.

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

%package GL
Summary:	OpenGL X screen savers
Summary(pl):	Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}
Requires:	OpenGL
Obsoletes:	xscreensaver-GL

%description GL
Screen savers which uses OpenGL libraries.

%description -l pl GL
Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL.

%package GLE
Summary:	OpenGL && GLE X screen savers
Summary(pl):	Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL && GLE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description GLE
Screen savers which uses OpenGL and GLE libraries.

%description -l pl GLE
Wygaszacze ekranu pod X Window u¿ywaj±ce OpenGL oraz GLE.

%prep
%setup  -q

%build
autoconf
# Build GNOME-free version.
%configure \
%ifarch alpha
	--without-xshm-ext \
%endif
	--without-motif \
	--with-gtk \
	--without-gnome \
	--with-pam \
	--with-dpms-ext \
	--with-gl \
	--with-gle \
	--enable-subdir=../lib/xscreensaver

%{__make}

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
	--with-gnome \
	--with-pam \
	--with-dpms-ext \
	--with-gl \
	--with-gle \
	--enable-subdir=../lib/xscreensaver

cd driver
%{__make} xscreensaver-demo
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pam.d \
	$RPM_BUILD_ROOT{%{_applnkdir}/{Settings/GNOME/Desktop,System},%{_datadir}/control-center/Desktop}

export KDEDIR=%{_prefix}
%{__make} install install_prefix=$RPM_BUILD_ROOT \
	AD_DIR=%{_libdir}/X11/app-defaults \
	PAM_DIR=/etc/pam.d \
	GNOME_CCDIR=%{_datadir}/control-center/Desktop \
	GNOME_PANELDIR=%{_applnkdir}/Settings/GNOME/Desktop

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install driver/xscreensaver $RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{_bindir}/xscreensaver-demo{,-gnome}
install driver/xscreensaver-demo-gnomefree $RPM_BUILD_ROOT%{_bindir}/xscreensaver-demo
%{__make} -C driver PAM_DIR=$RPM_BUILD_ROOT/etc/pam.d install-pam

install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xscreensaver

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
elif (echo "$_REQUIRES" | grep -q "libGLU.so"); then
	echo "%{_libdir}/xscreensaver/$file" >> $_DIR/files.gl
else
	echo "%{_libdir}/xscreensaver/$file" >> $_DIR/files.normal
fi
done

cd $_DIR

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.normal
%defattr(644,root,root,755)
%doc {README,README.debugging,screenblank.txt}.gz
%config %{_libdir}/X11/app-defaults/*
%{_applnkdir}/System/*
%{_pixmapsdir}/*.xpm
%attr(644,root,root) %config %verify(not size mtime md5) /etc/pam.d/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver
%attr(755,root,root) %{_bindir}/xscreensaver-command
%attr(755,root,root) %{_bindir}/xscreensaver-demo
%attr(755,root,root) %{_bindir}/xscreensaver-getimage*
%{_mandir}/man1/*
%dir %{_libdir}/xscreensaver

%files GL -f files.gl
%defattr(755,root,root)
%attr(755,root,root) %{_bindir}/xscreensaver-gl-helper

%files GLE -f files.gle
%defattr(755,root,root)
