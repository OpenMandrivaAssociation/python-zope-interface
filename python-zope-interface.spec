%define         tarname  zope.interface
%define		name python-zope-interface
%define 	version 3.3.0

Summary:        Zope Interface module for Python
Name:           %{name}
Version:        %{version}
Release:        %mkrel 1
Source0:        http://www.zope.org/Products/ZopeInterface/%{version}/%{tarname}-%{version}.tar.bz2
License:        Zope Public License
Group:          Development/Python
URL:            http://www.zope.org/Wikis/Interfaces/FrontPage
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
Requires:	python

%description
This package provides the zope Interface module.

Interfaces are objects that specify (document) the external behavior
of objects that "provide" them.  An interface specifies behavior
through: 

- Informal documentation in a doc string

- Attribute definitions

- Invariants, which are conditions that must hold for objects that
  provide the interface

Attribute definitions specify specific attributes. They define the
attribute name and provide documentation and constraints of attribute
values. Attribute definitions can take a number of forms.

%prep
%setup -q -n %{tarname}-%{version} 

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README.txt
%py_platsitedir/zope*
