%global python3_pkgversion 3
%global debug_package %{nil}
%global pypi_name TEMPLATE
%global package_dir_name TEMPLATE
%global github_name TEMPLATE
%global github_group TEMPLATE

Name: python-%{pypi_name}
Version: TEMPLATE
Release: 1%{?dist}
Summary: Some crazy stuff

License: MIT
URL: https://github.com/%{github_group}/%{name}/
Source0: https://github.com/%{github_group}/%{github_name}/archive/refs/tags/v%{version}.tar.gz/%{package_dir_name}-%{version}.tar.gz

BuildArch:      noarch

%description
IDGAF SO TODO

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n     python3-%{pypi_name}
IDGAF for python3-%{pypi_name}

%python_extras_subpkg -n python%{python3_pkgversion}-%{pypi_name} -i %{pyproject_files} EXTRANAME

%prep
%autosetup -p1 -n %{package_dir_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%py3_build

%install
%py3_install

%check
%tox || true

%files -n python3-%{pypi_name}
%doc CHANGES.txt README.rst
%license LICENSE
%{python3_sitelib}/%{package_dir_name}/
%{python3_sitelib}/%{package_dir_name}}-%{version}.dist-info/
%{python3_sitelib}/%{package_dir_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Jun 26 2025 Sergey Gorelov <infinity2573@gmail.com> 0.0.1
- Init version
