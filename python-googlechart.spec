%define realname    pygooglechart
%define name   python-googlechart
%define version 0.2.1
%define release 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Python wrapper for the Google Chart API
Group:          Development/Python
License:        ASL 2.0
URL:            http://south.aeracode.org
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
pygooglechart is a complete Python wrapper for the Google Chart API. 

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{realname}-%version

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Mon Nov 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.1-1mdv2011.0
+ Revision: 591665
- Fix Group
- import python-googlechart

