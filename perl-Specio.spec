#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Specio
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Specio - Test helpers for Specio
Summary(pl.UTF-8):	Test::Specio - pomocnicze funkcje i zmienne testowe dla Specio
Name:		perl-Specio
Version:	0.31
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Specio-%{version}.tar.gz
# Source0-md5:	7b3c109fbf6550e282ef77ccd9991e10
URL:		http://search.cpan.org/dist/Specio/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-StackTrace
BuildRequires:	perl-Eval-Closure
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Role-Tiny >= 1.003003
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Simple >= 0.96
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/TODO.pod \
	$RPM_BUILD_ROOT%{_mandir}/man3/TODO.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md TODO.pod
%{perl_vendorlib}/Specio
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Test/Specio.pm
%{_mandir}/man3/Specio*.3pm*
%{_mandir}/man3/Test::Specio.3pm*
