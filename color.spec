Summary:	ANSI coloring tool
Summary(pl):	Narzêdzie do kolorowania ANSI
Name:		color
Version:	1.1
Release:	3
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://runslinux.net/projects/color/%{name}-%{version}.tar.gz
# Source0-md5:	9131623568926877389aa0f6b95d939d
URL:		http://runslinux.net/projects.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color is a convenience tool to ease the use of ANSI coloring in your
shell scripts by hiding the escape sequences through command
substitution.

%description -l pl
Color jest wygodnym narzêdziem u³atwiaj±cym u¿ywanie kolorowania ANSI
w skryptach shellowych poprzez ukrycie sekwencji ANSI przed
u¿ytkownikiem, zastêpuj±c je podstawianiem komend.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install color $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/color
