# This specfile is licensed under:
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023 Wesley Gimenes <wehagy+github@gmail.com>
# See %%{name}.spec.license for the full license text.

%global SHA256SUM0      223c8da373a265de28591ba9269440c5cf79fa4f9168c00b99503a65982d4df1

%global provider        github
%global provider_tld    com
%global owner           vysp3r
%global repo            ProtonPlus
%global built_tag       v0.4.11
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version     %(b=%{built_tag_strip}; echo ${b/-/"."})

# com.vysp3r.ProtonPlus
%global flatpak_name    %{provider_tld}.%{owner}.%{repo}

# https://github.com/vysp3r/ProtonPlus
%global provider_prefix %{provider}.%{provider_tld}/%{owner}/%{repo}
%global import_path     %{provider_prefix}
%global git_repo        https://%{import_path}



Name:           protonplus
Version:        main
Release:        1%{?dist}
Summary:        Simple and powerful manager for Wine, Proton, DXVK and VKD3D

ExclusiveArch:  x86_64
License:        GPL-3.0-or-later
URL:            %{git_repo}
Source0:        %{url}/archive/refs/heads/%{version}.tar.gz
Source1:        %{name}.rpmlintrc
# License of the specfile
Source2:        %{name}.spec.license



BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.62.0
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)



# TLS support
Requires:       glib-networking



# Steam Tinker Launch support
Recommends:     wget
Recommends:     xdotool
Recommends:     xrandr
Recommends:     xwininfo
Recommends:     yad



%description
%{repo} is a simple and powerful manager for:
 - Wine
 - Proton
 - DXVK
 - VKD3D
 - Several other runners

Supports Steam, Lutris, Heroic and Bottles.



%prep
#echo "%%SHA256SUM0 %%{SOURCE0}" | sha256sum -c -
%autosetup -n %{repo}-%{version}



%build
%meson
%meson_build



%install
%meson_install
%find_lang %{flatpak_name}

# symlink prontonplus -> com.vysp3r.ProtonPlus
%{__ln_s} %{_bindir}/%{flatpak_name} %{buildroot}/%{_bindir}/%{name}



%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{flatpak_name}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{flatpak_name}.desktop



%files -f %{flatpak_name}.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
# install symlink prontonplus -> com.vysp3r.ProtonPlus
%{_bindir}/%{name}
%{_bindir}/%{flatpak_name}
%{_datadir}/applications/%{flatpak_name}.desktop
%{_datadir}/glib-2.0/schemas/%{flatpak_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{flatpak_name}.*
%{_metainfodir}/%{flatpak_name}.metainfo.xml



%changelog
* Sun Aug 04 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.11-1
- new upstream version v0.4.11

* Mon May 27 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.10-1
- new upstream version v0.4.10

* Wed Apr 10 2024 Wesley Gimenes <wehagy@proton.me> - 0.4.9-2
- build: rebuild for fedora 40 release

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.9-1
- new upstream version v0.4.9

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.8-1
- new upstream version v0.4.8

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7.2-1
- style: fixed indentation
- new upstream version v0.4.7-2

* Sun Dec 17 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7.1-1
- fix: change upstream version dash to dot
- fix: %%autosetup use upstream versioning
- new upstream version v0.4.7-1

* Sat Dec 16 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.7-1
- tighten dependencies
- removed unused files to accomodate new version
- new upstream version v0.4.7

* Sat Dec 16 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.6-3
- fix: incorrect day of week in changelog

* Thu Nov 09 2023 Wesley Gimenes <wehagy+github@gmail.com> - 0.4.6-3
- rebuild for fedora 39 release
- rename global variable project to owner
- add license to source of the specfile
- add SPDX license header

* Tue Sep 05 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-2
- rebuild v0.4.6-2 because of the file below
- fix: rename prontonplus-next.rpmlintrc to protonplus.rpmlintrc
- fix: change %%define to %%global
- fix: macros in changelog
- changed legacy license format to SPDX
- fix: W: dangerous-command-in-%%postun rm
- fix: W: dangerous-command-in-%%post ln
- fix: general improvements
- fix: E: standard-dir-owned-by-package
- fix: W: file-not-in-%%lang
- fix: W: no-manual-page-for-binary 
- fix: W: files-duplicate

* Mon Sep 04 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-2
- fix: use-of-RPM_SOURCE_DIR 

* Mon Sep 04 2023 Wesley H. Gimenes <wehagy+github@gmail.com> - 0.4.6-1
- First Release
