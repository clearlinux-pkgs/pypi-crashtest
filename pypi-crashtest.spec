#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-crashtest
Version  : 0.3.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/08/3c/5ec13020a4693fab34e1f438fe6e96aed6551740e1f4a5cc66e8b84491ea/crashtest-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/08/3c/5ec13020a4693fab34e1f438fe6e96aed6551740e1f4a5cc66e8b84491ea/crashtest-0.3.1.tar.gz
Summary  : Manage Python errors with ease
Group    : Development/Tools
License  : MIT
Requires: pypi-crashtest-license = %{version}-%{release}
Requires: pypi-crashtest-python = %{version}-%{release}
Requires: pypi-crashtest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: crashtest
Provides: crashtest-python
Provides: crashtest-python3
BuildRequires : pypi(poetry_core)

%description
# Crashtest
Crashtest is a Python library that makes exceptions handling and inspection easier.

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
%setup -q -n crashtest-0.3.1
cd %{_builddir}/crashtest-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641425407
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-crashtest
cp %{_builddir}/crashtest-0.3.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-crashtest/aa1d60525fded9648cab0e59a4338652671ad600
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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