%define name truckersmp-cli
%define version 0.10.1
%define release 1

Summary: A simple launcher for TruckersMP to be used with Wine/Proton
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source0: https://github.com/truckersmp-cli/truckersmp-cli/archive/refs/tags/%{version}.tar.gz
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Packager: badlydrawnface
Url: https://github.com/truckersmp-cli/truckersmp-cli
BuildRequires: python3 >= 3.6
BuildRequires: python3-setuptools
BuildRequires: mingw64-gcc
BuildRequires: make
Requires: python3 >= 3.6
Requires: python3-setuptools
Requires: SDL2
Requires: python3-vdf

%description
A simple launcher for TruckersMP to play ATS or ETS2 in multiplayer.

truckersmp-cli allows to download TruckersMP and handles starting TruckersMP through Wine while supporting the Windows versions of American Truck Simulator and Euro Truck Simulator 2.

The Windows version of Steam should already be able to run in the same Wine prefix. The Windows versions of ATS and ETS2 can be installed and updated via SteamCMD while all running Steam processes will be stopped to prevent Steam from loosing connection. Your Steam password and guard code are required by SteamCMD once for this to work.

On Linux it's possible to start TruckersMP through Proton. A working native Steam installation is needed for this which has the desired game installed or with an update pending. SteamCMD can use your saved credentials for convenience.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
make
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon May 8 2023 badlydrawnface <bdface@proton.me>
- 0.10.0 release of truckersmp-cli
* Thu Aug 4 2022 badlydrawnface <bdface@proton.me>
- Initial upload (version 0.9.1.1)
