#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-crashtest
Version  : 0.4.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/4a/d1/c08765bb40262491bf5da7c88b1a4ce62090c2a222a6ed706389277b6554/crashtest-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/d1/c08765bb40262491bf5da7c88b1a4ce62090c2a222a6ed706389277b6554/crashtest-0.4.0.tar.gz
Summary  : Manage Python errors with ease
Group    : Development/Tools
License  : MIT
Requires: pypi-crashtest-license = %{version}-%{release}
Requires: pypi-crashtest-python = %{version}-%{release}
Requires: pypi-crashtest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# Crashtest
[![Tests](https://github.com/sdispater/crashtest/actions/workflows/main.yml/badge.svg)](https://github.com/sdispater/crashtest/actions/workflows/main.yml)
[![PyPI version](https://img.shields.io/pypi/v/crashtest)](https://pypi.org/project/crashtest/)

%package license
Summary: license components for the pypi-crashtest package.
Group: Default

%description license
license components for the pypi-crashtest package.


%package python
Summary: python components for the pypi-crashtest package.
Group: Default
Requires: pypi-crashtest-python3 = %{version}-%{release}

%description python
python components for the pypi-crashtest package.


%package python3
Summary: python3 components for the pypi-crashtest package.
Group: Default
Requires: python3-core
Provides: pypi(crashtest)

%description python3
python3 components for the pypi-crashtest package.


%prep
%setup -q -n crashtest-0.4.0
cd %{_builddir}/crashtest-0.4.0
pushd ..
cp -a crashtest-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659647223
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-crashtest
cp %{_builddir}/crashtest-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-crashtest/aa1d60525fded9648cab0e59a4338652671ad600
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-crashtest/aa1d60525fded9648cab0e59a4338652671ad600

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
