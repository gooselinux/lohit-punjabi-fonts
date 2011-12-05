%global fontname lohit-punjabi
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.4
Release:        1%{?dist}
Summary:        Free Punjabi font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Punjabi truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
./generate.pe *.sfd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -rf %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Thu Apr 15 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- Resolves: bug 582156

* Tue Dec 29 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixed bug 548686, license field
- Resolves: bug 551014

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.3-2.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
