%define		qtver		4.8.5

Summary:	pavucontrol-qt
Name:		pavucontrol-qt
Version:	0.1.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/pavucontrol-qt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	32217c5ae8a846e92548a55b8d3b9267
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	glib2-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pavucontrol-qt

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pavucontrol-qt
%{_desktopdir}/pavucontrol-qt.desktop
