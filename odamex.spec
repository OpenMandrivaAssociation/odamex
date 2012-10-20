# norootforbuild

Name: odamex
Summary: Odamex is a free and open source port for the classic first-person-shooter Doom
Version: 0.6.1
Release: %mkrel 1
License: GPL
Group:  Games/Arcade  
URL: http://odamex.net/
Source0: odamex-src-0.6.1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: make autoconf automake gcc gcc-c++

BuildRequires: fdupes 

BuildRequires: SDL-devel SDL_mixer-devel audiofile-devel
BuildRequires: glibc-devel libstdc++-devel libmikmod-devel X11-devel unzip wxGTK-devel

%description
Odamex is a free and open source port for the classic first-person-shooter Doom.
Odamex's goal is to emulate the feel of and retain many aspects of the original
Doom executables while offering a broader expanse of security features,
personal configuration, gameplay options, and editing features.


%prep
%setup -q -n odamex-src-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%__make

%install
%makeinstall

%__cp %{buildroot}%{_datadir}/doom/odamex.wad %{buildroot}%{_gamesdatadir}/odamex.wad

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{_gamesdatadir}/doom
%{_gamesdatadir}/doom/*.wad

