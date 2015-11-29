Name:		python-xmlrpc_negotiate
Version:	1.0
Release:	1%{?dist}
BuildArch:	noarch
Summary:	HTTP Negotiate auth for XMLRPC

License:	MIT
Source0:	xmlrpc_negotiate-%{version}.tar.gz

Requires: python-kerberos

%description
Provides kerberos based HTTP Negotiate auth for python XMLRPC client


%prep
%setup -q


%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files
%{python_sitelib}/xmlrpc_negotiate.py
%{python_sitelib}/xmlrpc_negotiate.pyc
%{python_sitelib}/xmlrpc_negotiate.py-*.egg-info


%changelog

