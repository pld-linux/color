Summary:	ANSI coloring tool
Summary(pl):	Narzêdzie do kolorowaia ANSI
Name:		color
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://runslinux.net/projects/color/color-1.1.tar.gz
URL:		http://runslinux.net/projects.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Color is a convenience tool to ease the use of ANSI coloring in your shell
scripts by hiding the escape sequences through command substitution.

%description -l pl
Color jest wygodnym narzêdziem u³atwiaj±cym u¿ywanie kolorowania ANSI w 
skryptach shellowych poprzez ukrycie sekwencji ANSI przed u¿ytkownikiem,
zastêpuj±c je podstawianiem komend.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install color $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/color
%doc *.gz
