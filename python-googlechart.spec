%define realname    pygooglechart
%define name   python-googlechart
%define version 0.2.1
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Python wrapper for the Google Chart API
Group:          Development/Languages
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

