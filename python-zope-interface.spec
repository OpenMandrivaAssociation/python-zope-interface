%define         tarname  ZopeInterface

Summary:        A zope module providing 
Name:           python-zope-interface
Version:        3.0.1
Release:        %mkrel 2
Source0:        http://www.zope.org/Products/ZopeInterface/3.0.1final/%{tarname}-%{version}.tar.bz2
Patch:          python-zope-interface.gcc4.patch
License:        Zope Public License
Group:          Development/Python
URL:            http://www.zope.org/Wikis/Interfaces/FrontPage
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel

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
values. Attribute definitions can take a number of forms, as we'll
see below.

%prep
%setup -q -n %{tarname}-%{version} 
%patch0

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


