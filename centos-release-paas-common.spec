Summary:   Common release file to establish shared metadata for CentOS PaaS SIG
Name:      centos-release-paas-common
Version:   1
Release:   1%{?dist}
License:   GPL
Group:     System Environment/Base
Source0:   RPM-GPG-KEY-CentOS-SIG-PaaS
URL:       https://wiki.centos.org/SpecialInterestGroup/PaaS
BuildArch: noarch

Provides:  centos-release-paas-common
Requires:  centos-release

%description
Common files needed by other centos-release components in the PaaS SIG

%prep
%setup -q -n %{name} -T -c

%install
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%files
%license LICENSE
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Storage

%changelog
* Wed May 18 2016 Troy Dawson <tdawson@redha.com> - 1-1
- Basic setup with the gpg key
- Based on the centos-release-storage-common package