#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Specio
Summary:	Test::Specio - Test helpers for Specio
Summary(pl.UTF-8):	Test::Specio - pomocnicze funkcje i zmienne testowe dla Specio
Name:		perl-Specio
Version:	0.46
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Specio-%{version}.tar.gz
# Source0-md5:	aca3a183b46b93a8ce02009a2ccd868b
URL:		https://metacpan.org/release/Specio
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Devel-StackTrace
BuildRequires:	perl-Eval-Closure
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Role-Tiny >= 1.003003
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Storable
BuildRequires:	perl-Sub-Quote
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-version >= 0.83
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides some helper functions and variables for testing
Specio types.

%description -l pl.UTF-8
Ten pakiet dostarcza kilka pomocniczych funkcji i zmiennych do
testowania typów Specio.

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
%doc Changes README.md TODO.md
%{perl_vendorlib}/Specio
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Test/Specio.pm
%{_mandir}/man3/Specio*.3pm*
%{_mandir}/man3/Test::Specio.3pm*
