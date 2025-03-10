
%define		module	PyQtWebEngine
# minimal required sip version
%define		sip_ver	6.4
# last qt version covered by these bindings (minimal required is currently 5.0.0)
# %define		qt_ver	%{version}
%define		qt_ver	5.15.0

Summary:	Python bindings for the Qt5WebEngine module
Summary(pl.UTF-8):	Wiązania Pythona do modułu Qt5WebEngine
Name:		python3-%{module}
Version:	5.15.7
Release:	2
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
# Source0-md5:	a3394e93d8b5077e8355f57d79c2ed58
URL:		http://www.riverbankcomputing.com/software/pyqtwebengine/
BuildRequires:	Qt5WebEngine-devel >= %{qt_ver}
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt5
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip-PyQt5 >= 5.15.7
BuildRequires:	sip6 >= %{sip_ver}
Requires:	python3-libs
Obsoletes:	python-PyQtWebEngine < 5.15.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the Qt5WebEngine module.

%description -l pl.UTF-8
Wiązania Pythona do modułu Qt5WebEngine.

%package -n sip-PyQtWebEngine
Summary:	SIP files needed to build bindings for Qt5WebEngine
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania wiązań do Qt5WebEngine
Group:		Development/Languages/Python
Requires:	python3-PyQt5-sip >= 2:12.11.0
Requires:	sip6 >= %{sip_ver}

%description -n sip-PyQtWebEngine
SIP files needed to build bindings for Qt5WebEngine.

%description -n sip-PyQtWebEngine -l pl.UTF-8
Pliki SIP potrzebne do budowania wiązań do Qt5WebEngine.

%prep
%setup -q -n PyQtWebEngine-%{version}

%build
sip-build --build-dir build-py3 \
	--jobs %{__jobs} \
	--verbose \
	--pep484-pyi \
	--qmake="%{_bindir}/qmake-qt5" \
	--scripts-dir=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-py3 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngine.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngineCore.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngineWidgets.abi3.so
%{py3_sitedir}/PyQt5/QtWebEngine.pyi
%{py3_sitedir}/PyQt5/QtWebEngineCore.pyi
%{py3_sitedir}/PyQt5/QtWebEngineWidgets.pyi
%{py3_sitedir}/PyQtWebEngine-%{version}.dist-info

%files -n sip-PyQtWebEngine
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings/QtWebEngine
%{py3_sitedir}/PyQt5/bindings/QtWebEngineCore
%{py3_sitedir}/PyQt5/bindings/QtWebEngineWidgets
