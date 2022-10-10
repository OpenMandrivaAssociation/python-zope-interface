%define debug_package %nil
%define	tarname  zope.interface
%bcond_with python2

Summary:	Zope Interface module for Python

Name:		python-zope-interface
Version:	5.5.0
Release:	1
License:	Zope Public License
Group:		Development/Python
Url:		https://github.com/zopefoundation/zope.interface
Source0:	https://github.com/zopefoundation/zope.interface/archive/%{version}.tar.gz
Source100: %{name}.rpmlintrc
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
%if %{with python2}
BuildRequires:	pkgconfig(python)
BuildRequires:	python2-setuptools
BuildRequires:	python2-pkg-resources
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

%if %{with python2}
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
%endif

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
%{py_platsitedir}/zope
%{py_platsitedir}/zope.interface-%{version}-*.egg-info
%{py_platsitedir}/zope.interface-*.pth

%if %{with python2}
%files -n python2-zope-interface
%{py2_platsitedir}/zope
%{py2_platsitedir}/zope.interface-%{version}-*.egg-info
%{py2_platsitedir}/zope.interface-*.pth
%endif
