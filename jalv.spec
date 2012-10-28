Summary:	LV2 host for jack
Name:		jalv
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/jalv-%{version}.tar.bz2
# Source0-md5:	babb0ffb0f5083d87b93def98880579d
BuildRequires:	QtGui-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtkmm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblilv-devel
BuildRequires:	libserd-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libsuil-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jalv is a simple but fully featured LV2 host for Jack.
It runs LV2 plugins and exposes their ports as Jack ports,
essentially making any LV2 plugin function as a Jack application.

%prep
%setup -q

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
	--nocache \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/jalv
%attr(755,root,root) %{_bindir}/jalv.gtk
# not fully working
#%attr(755,root,root) %{_bindir}/jalv.gtk3
#%attr(755,root,root) %{_bindir}/jalv.gtkmm
#%attr(755,root,root) %{_bindir}/jalv.qt
%{_mandir}/man1/jalv.1*
%{_mandir}/man1/jalv.gtk.1*
#%{_mandir}/man1/jalv.gtkmm.1*
#%{_mandir}/man1/jalv.qt.1*

