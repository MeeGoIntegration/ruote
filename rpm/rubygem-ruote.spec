#
# spec file for package rubygem-ruote (Version 2.1.10)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-ruote
Version:        2.2.0
Release:        0
%define mod_name ruote
#
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-sourcify >= 0.4.2
Requires:       rubygem-sourcify >= 0.4.2
BuildRequires:  rubygem-rufus-json >= 0.2.2
Requires:       rubygem-rufus-json >= 0.2.2
BuildRequires:  rubygem-rufus-cloche >= 0.1.17
Requires:       rubygem-rufus-cloche >= 0.1.17
BuildRequires:  rubygem-rufus-dollar 
Requires:       rubygem-rufus-dollar 
BuildRequires:  rubygem-rufus-mnemo >= 1.1.0
Requires:       rubygem-rufus-mnemo >= 1.1.0
BuildRequires:  rubygem-rufus-scheduler >= 2.0.5
Requires:       rubygem-rufus-scheduler >= 2.0.5
BuildRequires:  rubygem-rufus-treechecker >= 1.0.3
Requires:       rubygem-rufus-treechecker >= 1.0.3
#
Url:            http://ruote.rubyforge.org
Source:         %{mod_name}-%{version}.gem
#
Summary:        an open source ruby workflow engine
%description

ruote is an open source ruby workflow engine.
    

%prep
%build
%install
%gem_install %{S:0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
