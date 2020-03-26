Name: nethserver-openssh
Summary: sshd daemon configuration
Version: 1.5.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 
BuildRequires: nethserver-devtools
Requires: openssh-server
Requires: nethserver-base
Requires: pam_oath

%description
Configure and manage the sshd daemon

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
( cd root ; find . -depth -print | cpio -dump %{buildroot} )
%{genfilelist} %{buildroot}  > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update


%changelog
* Wed Mar 25 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.5.0-1
- Openssh: Protect password login with 2FA - NethServer/dev#6088

* Thu Feb 27 2020 Davide Principi <davide.principi@nethesis.it> - 1.4.1-1
- SSH login failure with conflicting group permissions - Bug NethServer/dev#6058
- Allow everyone to use SFTP and restrict SSH port forwarding - NethServer/dev#6059

* Wed Jan 29 2020 Davide Principi <davide.principi@nethesis.it> - 1.4.0-1
- Group-based access restriction for Cockpit and SSH  - NethServer/dev#6029

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.0-1
- Revert OpenSSH TLS policy configuration - NethServer/dev#5835

* Tue Apr 03 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.2-1
- Hardening TLS policy 2018-03-30 - NethServer/dev#5438

* Mon Apr 10 2017 Davide Principi <davide.principi@nethesis.it> - 1.2.1-1
- Add  /root/.ssh directory to backup-config - NethServer/dev#5264

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.0-1
- First NS7 release

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Tue Mar 03 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- SSH: locked out of 6.6 beta1 - Bug #3015 [NethServer]
- Base: first configuration wizard - Feature #2957 [NethServer]

* Tue Dec 09 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.8-1.ns6
- ssh access remains public when set to private - Bug #2970 [NethServer]
- Release file and MOTD - Enhancement #2845 [NethServer]
- Drop TCP wrappers hosts.allow hosts.deny templates - Enhancement #2785 [NethServer]

* Tue Oct 28 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.7-1.ns6
- Remote access: web interface error when changing the SSH port - Bug #2847 [NethServer]

* Wed Oct 15 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1.ns6
- Backup config: list only relevant files - Feature #2739

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.5-1.ns6
- Removed fs executable bit from UI language catalogs.

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.4-1.ns6
- Default remote access from public networks - Enhancement #2548 [NethServer]
- SSH: connection keep alive - Enhancement #2147 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Wed Oct 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Fix expansion of lokkit template #2205
- SSG daemon should listen on 0.0.0.0 #2138
- Db defaults: remove Runlevels prop #2067

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870
- Restart sshd when changing port. #1862

* Mon Mar 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- First release
