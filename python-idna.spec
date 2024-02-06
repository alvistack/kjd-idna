# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-idna
Epoch: 100
Version: 3.6
Release: 1%{?dist}
BuildArch: noarch
Summary: Internationalized Domain Names in Applications (IDNA)
License: BSD-3-Clause
URL: https://github.com/kjd/idna/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Support for the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This is the latest version of the
protocol and is sometimes referred to as “IDNA 2008”. This library also
provides support for Unicode Technical Standard 46, Unicode IDNA
Compatibility Processing. This acts as a suitable replacement for the
“encodings.idna” module that comes with the Python standard library,
but which only supports the old, deprecated IDNA specification (RFC
3490).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-idna
Summary: Internationalized Domain Names in Applications (IDNA)
Requires: python3
Provides: python3-idna = %{epoch}:%{version}-%{release}
Provides: python3dist(idna) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-idna = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(idna) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-idna = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(idna) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-idna
Support for the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This is the latest version of the
protocol and is sometimes referred to as “IDNA 2008”. This library also
provides support for Unicode Technical Standard 46, Unicode IDNA
Compatibility Processing. This acts as a suitable replacement for the
“encodings.idna” module that comes with the Python standard library,
but which only supports the old, deprecated IDNA specification (RFC
3490).

%files -n python%{python3_version_nodots}-idna
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-idna
Summary: Internationalized Domain Names in Applications (IDNA)
Requires: python3
Provides: python3-idna = %{epoch}:%{version}-%{release}
Provides: python3dist(idna) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-idna = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(idna) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-idna = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(idna) = %{epoch}:%{version}-%{release}

%description -n python3-idna
Support for the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891. This is the latest version of the
protocol and is sometimes referred to as “IDNA 2008”. This library also
provides support for Unicode Technical Standard 46, Unicode IDNA
Compatibility Processing. This acts as a suitable replacement for the
“encodings.idna” module that comes with the Python standard library,
but which only supports the old, deprecated IDNA specification (RFC
3490).

%files -n python3-idna
%license LICENSE.md
%{python3_sitelib}/*
%endif

%changelog
