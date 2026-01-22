%define	tarname  zope.interface

Name:		python-zope-interface
Version:	8.2
Release:	1
Summary:	Zope Interface module for Python
License:	ZPL-2.1
Group:		Development/Python
URL:			https://github.com/zopefoundation/zope.interface
Source0:	https://github.com/zopefoundation/zope.interface/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100: %{name}.rpmlintrc
BuildSystem:  python
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# other packages require this provides
Provides: python%{pyver}dist(zope-interface) = %{version}-%{release}

# Obsolete old duplicated package
%rename python-zope.interface

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

%build -p
export LDFLAGS="%{optflags} -lpython%{pyver}"

%files
%doc README.rst
%license LICENSE.txt COPYRIGHT.txt
%{python_sitearch}/zope
%{python_sitearch}/zope_interface-%{version}.dist-info
