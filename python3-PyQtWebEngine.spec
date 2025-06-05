#
# Conditional build:
%bcond_without	obsolete_py2	# obsolete python-PyQtWebEngine package

%define		module	PyQtWebEngine
# minimal required sip version
%define		sip_ver	6.8
# last qt version covered by these bindings (minimal required is currently 5.4.0)
# see sip/QtWebEngineCore/QtWebEngineCoremod.sip /%Timeline
%define		qt_ver	5.15.0

Summary:	Python bindings for the Qt5WebEngine module
Summary(pl.UTF-8):	Wiązania Pythona do modułu Qt5WebEngine
Name:		python3-%{module}
Version:	5.15.7
Release:	5
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyqtwebengine/
Source0:	https://files.pythonhosted.org/packages/source/P/PyQtWebEngine/PyQtWebEngine-%{version}.tar.gz
# Source0-md5:	a3394e93d8b5077e8355f57d79c2ed58
URL:		https://www.riverbankcomputing.com/software/pyqtwebengine/
BuildRequires:	Qt5WebEngine-devel >= %{qt_ver}
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt-builder >= 1.9
BuildRequires:	python3-PyQt-builder < 2
BuildRequires:	python3-PyQt5 >= 5.15.4
BuildRequires:	python3-PyQt5-devel >= 5.15.4
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sip6 >= %{sip_ver}
Requires:	python3-libs
%if %{with obsolete_py2}
Obsoletes:	python-PyQtWebEngine < 5.15.6
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the Qt5WebEngine module.

%description -l pl.UTF-8
Wiązania Pythona do modułu Qt5WebEngine.

%package devel
Summary:	SIP files needed to build bindings for Qt5WebEngine
Summary(pl.UTF-8):	Pliki SIP potrzebne do budowania wiązań do Qt5WebEngine
Group:		Development/Languages/Python
Requires:	python3-PyQt5-devel >= 5.15.4
Requires:	sip6 >= %{sip_ver}
%if %{with obsolete_py2}
Obsoletes:	sip-PyQtWebEngine < 5.15.7-5
%else
# >= 5.15.7-1 && < 5.15.7-5, but boolean expressions are not supported for Obsoletes
Obsoletes:	sip-PyQtWebEngine >= 5.15.7
%endif

%description devel
SIP files needed to build bindings for Qt5WebEngine.

%description devel -l pl.UTF-8
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
%doc ChangeLog NEWS README.md
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngine.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngineCore.abi3.so
%attr(755,root,root) %{py3_sitedir}/PyQt5/QtWebEngineWidgets.abi3.so
%{py3_sitedir}/PyQt5/QtWebEngine.pyi
%{py3_sitedir}/PyQt5/QtWebEngineCore.pyi
%{py3_sitedir}/PyQt5/QtWebEngineWidgets.pyi
%{py3_sitedir}/pyqtwebengine-%{version}.dist-info

%files devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings/QtWebEngine
%{py3_sitedir}/PyQt5/bindings/QtWebEngineCore
%{py3_sitedir}/PyQt5/bindings/QtWebEngineWidgets
