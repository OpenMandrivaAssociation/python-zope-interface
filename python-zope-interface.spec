%define	tarname  zope.interface

Summary:        Zope Interface module for Python
Name:           python-zope-interface
Version:        4.0.5
Release:        1
Source0:        http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.zip
License:        Zope Public License
Group:          Development/Python
URL:            http://www.zope.org/Wikis/Interfaces/FrontPage
BuildRequires:	python-devel
BuildRequires:	python-setuptools

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir} 

%files
%doc *.txt
%py_platsitedir/*

