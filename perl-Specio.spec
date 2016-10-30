#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Specio
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Specio - Test helpers for Specio
Name:		perl-Specio
Version:	0.30
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Specio-%{version}.tar.gz
# Source0-md5:	a13555cdf2f17b275ec5edccac58bf64
URL:		http://search.cpan.org/dist/Specio/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-StackTrace
BuildRequires:	perl-Eval-Closure
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Role-Tiny
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some helper functions and variables for testing
Specio types.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%{perl_vendorlib}/Specio
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Test/Specio.pm
%{_mandir}/man3/Specio*.3pm*
%{_mandir}/man3/Test::Specio.3pm*
