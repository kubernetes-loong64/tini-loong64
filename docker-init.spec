Name: docker-init
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: A tiny but valid docker-init for containers (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/tini-loong64
BugURL: https://github.com/kubernetes-loong64/tini-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
Tini is the simplest docker-init you could think of. All it does is spawn a
single child (Tini is meant to be run in a container), and wait for it
to exit, all the while reaping zombies and performing signal forwarding.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 docker-init %{buildroot}/usr/bin/docker-init

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/docker-init

%changelog
