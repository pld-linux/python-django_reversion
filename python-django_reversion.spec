%define		module		reversion
Summary:	Flexible Version Control for Django
Name:		python-django_reversion
Version:	1.3.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://django-reversion.googlecode.com/files/django-%{module}-%{version}.tar.gz
# Source0-md5:	2d1cf38ac0da500cb776394499f5998e
URL:		http://code.google.com/p/django-reversion/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
Requires:	python-django >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

Features

- Roll back to any point in a model's history - an unlimited undo
  facility!
- Recover deleted models - never lose data again!
- Admin integration for maximum usability.
- Group related changes into revisions that can be rolled back in a
  single transaction.
- Automatically save a new version whenever your model changes using
  Django's flexible signalling framework.
- Automate your revision management with easy-to-use middleware.

Reversion can be easily added to your existing Django project with an
absolute minimum of code changes.

%prep
%setup -q -n django-%{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/django_reversion-%{version}-*.egg-info
