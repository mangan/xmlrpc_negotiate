%global srcname xmlrpc_negotiate
Name:		python-%{srcname}
Version:	1.0
Release:	1%{?dist}
Summary:	HTTP Negotiate auth for XMLRPC

License:	MIT
Source0:	%{srcname}-%{version}.tar.gz

BuildRequires:	python
Requires:	python-kerberos


%description
Provides kerberos based HTTP Negotiate auth for python XMLRPC client


%prep
%setup -n %{srcname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files
%{python_sitelib}/xmlrpc_negotiate.py*
%{python_sitelib}/%{srcname}-*.egg-info


%changelog

