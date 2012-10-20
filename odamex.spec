# norootforbuild

Name: odamex
Summary: Odamex is a free and open source port for the classic first-person-shooter Doom
Version: 0.4.2
Release: 15.37
License: GPL
Group:  Amusements/Games/Action/Shoot  
URL: http://odamex.net/
Source0: odamex-src-0.4.2.tar.bz2
Source1: freedoom-iwad-0.6.2.zip
Patch0: odamex-0.4.2-DESTDIR.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: make autoconf automake gcc gcc-c++
%if %suse_version > 1020
BuildRequires: fdupes 
%endif
BuildRequires: SDL-devel SDL_mixer-devel audiofile-devel
BuildRequires: glibc-devel libstdc++-devel libmikmod-devel xorg-x11-devel unzip wxGTK-devel

%description
Odamex is a free and open source port for the classic first-person-shooter Doom.
Odamex's goal is to emulate the feel of and retain many aspects of the original
Doom executables while offering a broader expanse of security features,
personal configuration, gameplay options, and editing features.

%debug_package
%prep
%setup -q -n odamex-src-0.4.2
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%__make

%install
%makeinstall

%__cp %{buildroot}%{_datadir}/doom/odamex.wad %{buildroot}%{_bindir}/odamex.wad

pushd %{buildroot}%{_datadir}/doom/
%__unzip -o "%{SOURCE1}"
popd

%__mv  %{buildroot}%{_datadir}/doom/freedoom-iwad-0.6.2/*.wad %{buildroot}%{_datadir}/doom/
%__rm -rf  %{buildroot}%{_datadir}/doom/freedoom-iwad-0.6.2

%if %suse_version > 1020
%fdupes -s %{buildroot}
%endif

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{_datadir}/doom
%{_datadir}/doom/*.wad

