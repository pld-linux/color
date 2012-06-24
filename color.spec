Summary:	ANSI coloring tool
Summary(pl):	Narz�dzie do kolorowania ANSI
Name:		color
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://runslinux.net/projects/color/%{name}-%{version}.tar.gz
# Source0-md5:	17938f68c0ad3060111446c34922fdf2
URL:		http://runslinux.net/?page_id=10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color is a convenience tool to ease the use of ANSI coloring in your
shell scripts by hiding the escape sequences through command
substitution.

%description -l pl
Color jest wygodnym narz�dziem u�atwiaj�cym u�ywanie kolorowania ANSI
w skryptach shellowych poprzez ukrycie sekwencji ANSI przed
u�ytkownikiem, zast�puj�c je podstawianiem komend.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install color $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/color
