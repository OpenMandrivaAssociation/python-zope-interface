%define	tarname  zope.interface
%bcond_without python2

Summary:	Zope Interface module for Python

Name:		python-zope-interface
Version:	4.1.1
Release:	6
License:	Zope Public License
Group:		Development/Python
Url:		http://www.zope.org/Wikis/Interfaces/FrontPage
Source0:	http://pypi.python.org/packages/source/z/zope.interface/zope.interface-%{version}.tar.gz
Source100: %{name}.rpmlintrc
BuildRequires:	pkgconfig(python3)
%if %{with python2}
BuildRequires:	pkgconfig(python)
%endif

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

%package -n python2-zope-interface
Summary:	Zope Interface module for Python 2.x
Group:		Development/Python

%description -n python2-zope-interface
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
mkdir python3
mv `ls |grep -v python3` python3
%if %{with python2}
cp -a python3 python2
%endif

%build
cd python3
%__python setup.py build

%if %{with python2}
cd ../python2
python2 setup.py build
%endif

%install
cd python3
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir} 

%if %{with python2}
cd ../python2
PYTHONDONTWRITEBYTECODE= python2 setup.py install --root=%{buildroot} --install-purelib=%{py2_platsitedir} 
%endif

%files
%doc python3/*.txt
%{py_platsitedir}/*

%files -n python2-zope-interface
%{py2_platsitedir}/*
