%define	tarname  zope.interface

Summary:	Zope Interface module for Python

Name:		python-zope-interface
Version:	4.1.1
Release:	3
License:	Zope Public License
Group:		Development/Python
Url:		http://www.zope.org/Wikis/Interfaces/FrontPage
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
Source100: %{name}.rpmlintrc
BuildRequires:	pkgconfig(python3)

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
%setup -qn %{tarname}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir} 

%files
%doc *.txt
%{py_platsitedir}/*
