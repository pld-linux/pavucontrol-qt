%define		qtver		6.6.0

Summary:	Qt port of volume control pavucontrol
Summary(pl.UTF-8):	Port Qt regulacji głośności pavucontrol
Name:		pavucontrol-qt
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	https://github.com/lxqt/pavucontrol-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2d6a82e01b3184ed3a914fabe7d0cefb
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	perl-base
BuildRequires:	pulseaudio-devel
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt port of volume control pavucontrol.

%description -l pl.UTF-8
Port Qt regulacji głośności pavucontrol.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pavucontrol-qt
%{_desktopdir}/pavucontrol-qt.desktop
%dir %{_datadir}/pavucontrol-qt
# required for the lang files
%dir %{_datadir}/pavucontrol-qt/translations
