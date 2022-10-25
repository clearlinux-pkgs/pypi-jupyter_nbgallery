#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_nbgallery
Version  : 2.0.0
Release  : 58
URL      : https://files.pythonhosted.org/packages/54/ed/24e5101d7d296f02cb8b45ebdecb9858f7a0ec44762b3037f0b404c8aced/jupyter-nbgallery-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/54/ed/24e5101d7d296f02cb8b45ebdecb9858f7a0ec44762b3037f0b404c8aced/jupyter-nbgallery-2.0.0.tar.gz
Summary  : Jupyter extensions to add nbgallery integration
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-jupyter_nbgallery-bin = %{version}-%{release}
Requires: pypi-jupyter_nbgallery-data = %{version}-%{release}
Requires: pypi-jupyter_nbgallery-license = %{version}-%{release}
Requires: pypi-jupyter_nbgallery-python = %{version}-%{release}
Requires: pypi-jupyter_nbgallery-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_server)

%description
# Overview

%package bin
Summary: bin components for the pypi-jupyter_nbgallery package.
Group: Binaries
Requires: pypi-jupyter_nbgallery-data = %{version}-%{release}
Requires: pypi-jupyter_nbgallery-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_nbgallery package.


%package data
Summary: data components for the pypi-jupyter_nbgallery package.
Group: Data

%description data
data components for the pypi-jupyter_nbgallery package.


%package license
Summary: license components for the pypi-jupyter_nbgallery package.
Group: Default

%description license
license components for the pypi-jupyter_nbgallery package.


%package python
Summary: python components for the pypi-jupyter_nbgallery package.
Group: Default
Requires: pypi-jupyter_nbgallery-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_nbgallery package.


%package python3
Summary: python3 components for the pypi-jupyter_nbgallery package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_nbgallery)
Requires: pypi(jupyter_server)

%description python3
python3 components for the pypi-jupyter_nbgallery package.


%prep
%setup -q -n jupyter-nbgallery-2.0.0
cd %{_builddir}/jupyter-nbgallery-2.0.0
pushd ..
cp -a jupyter-nbgallery-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656396670
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_nbgallery
cp %{_builddir}/jupyter-nbgallery-2.0.0/jupyter_nbgallery/nbextensions/instrumentation/crypto-js-license.txt %{buildroot}/usr/share/package-licenses/pypi-jupyter_nbgallery/1d0d2968b35836cde91ab65b1692d1546ffa4fb3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_notebook_config.d %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/nbconfig/notebook.d  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/nbconfig/common.d %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_server_config.d %{buildroot}/usr/share/jupyter/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-nbgallery

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/common.d/jupyter_nbgallery.json
/usr/share/jupyter/jupyter_notebook_config.d/jupyter_nbgallery.json
/usr/share/jupyter/jupyter_server_config.d/jupyter_nbgallery.json
/usr/share/jupyter/nbextensions/jupyter_nbgallery/autodownload/README.md
/usr/share/jupyter/nbextensions/jupyter_nbgallery/autodownload/autodownload.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/autodownload/autodownload.png
/usr/share/jupyter/nbextensions/jupyter_nbgallery/autodownload/autodownload.yaml
/usr/share/jupyter/nbextensions/jupyter_nbgallery/easy_buttons/README.md
/usr/share/jupyter/nbextensions/jupyter_nbgallery/easy_buttons/easy_buttons.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/easy_buttons/easy_buttons.png
/usr/share/jupyter/nbextensions/jupyter_nbgallery/easy_buttons/easy_buttons.yaml
/usr/share/jupyter/nbextensions/jupyter_nbgallery/environment/README.md
/usr/share/jupyter/nbextensions/jupyter_nbgallery/environment/environment.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/environment/environment.yaml
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/README.md
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/bootbox.min.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/gallery_menu.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/gallery_menu.yaml
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/gallery_menu_1.png
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/gallery_menu_2.png
/usr/share/jupyter/nbextensions/jupyter_nbgallery/gallery_menu/preferences_menu.png
/usr/share/jupyter/nbextensions/jupyter_nbgallery/instrumentation/README.md
/usr/share/jupyter/nbextensions/jupyter_nbgallery/instrumentation/crypto-js-license.txt
/usr/share/jupyter/nbextensions/jupyter_nbgallery/instrumentation/instrumentation.js
/usr/share/jupyter/nbextensions/jupyter_nbgallery/instrumentation/instrumentation.yaml
/usr/share/jupyter/nbextensions/jupyter_nbgallery/instrumentation/md5.js
/usr/share/jupyter/notebook.d/jupyter_nbgallery.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_nbgallery/1d0d2968b35836cde91ab65b1692d1546ffa4fb3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
