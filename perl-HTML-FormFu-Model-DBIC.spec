#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	HTML
%define	pnam	FormFu-Model-DBIC
Summary:	HTML::FormFu::Model::DBIC - Integrate HTML::FormFu with DBIx::Class
Summary(pl.UTF-8):	HTML::FormFu::Model::DBIC - integruje HTML::FormFu z DBIx::Class
Name:		perl-HTML-FormFu-Model-DBIC
Version:	0.05002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aba55f669530e02b421632da95c03f6b
URL:		http://search.cpan.org/dist/HTML-FormFu-Model-DBIC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBIx-Class >= 0.08106
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-HTML-FormFu >= 0.05000
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Task-Weaken
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormFu::Model::DBIC integrates HTML::FormFu with DBIx::Class.

%description -l pl.UTF-8
HTML::FormFu::Model::DBIC integruje HTML::FormFu z DBIx::Class.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%dir %{perl_vendorlib}/HTML/FormFu/Model
%{perl_vendorlib}/HTML/FormFu/Model/*.pm
%{_mandir}/man3/*
