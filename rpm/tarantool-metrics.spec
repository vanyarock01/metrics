Name: tarantool-metrics
Version: 1.0.0
Release: 1%{?dist}
Summary: Tool to collect metrics with Tarantool
Group: Applications/Databases
License: MIT
URL: https://github.com/tarantool/metrics
Source0: https://github.com/tarantool/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: tarantool >= 1.7.5.0
Requires: tarantool-checks >= 2.1.0.0
%description
Easy collecting, storing and manipulating metrics timeseriess.

%define luapkgdir %{_datadir}/tarantool
%define br_luapkgdir %{buildroot}%{luapkgdir}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{br_luapkgdir}
cp -rv metrics %{br_luapkgdir}

%files
%dir %{luapkgdir}/metrics
     %{luapkgdir}/metrics/init.lua
%dir %{luapkgdir}/metrics/details
     %{luapkgdir}/metrics/details/init.lua
%dir %{luapkgdir}/metrics/plugins
     %{luapkgdir}/metrics/plugins/README.md
%dir %{luapkgdir}/metrics/plugins/prometheus
     %{luapkgdir}/metrics/plugins/prometheus/init.lua
     %{luapkgdir}/metrics/plugins/prometheus/README.md
%dir %{luapkgdir}/metrics/plugins/graphite
     %{luapkgdir}/metrics/plugins/graphite/init.lua
     %{luapkgdir}/metrics/plugins/graphite/README.md
%dir %{luapkgdir}/metrics/plugins/json
     %{luapkgdir}/metrics/plugins/json/init.lua
     %{luapkgdir}/metrics/plugins/json/README.md
%dir %{luapkgdir}/metrics/server
     %{luapkgdir}/metrics/server/init.lua
     %{luapkgdir}/metrics/server/README.md
%dir %{luapkgdir}/metrics/default_metrics
%dir %{luapkgdir}/metrics/default_metrics/tarantool
     %{luapkgdir}/metrics/default_metrics/tarantool/fibers.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/info.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/init.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/memory.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/network.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/operations.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/replicas.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/runtime.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/slab.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/spaces.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/system.lua
     %{luapkgdir}/metrics/default_metrics/tarantool/utils.lua

%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE


%changelog
* Thu Mar 07 2019 Elizaveta Dokshina <dokshina@tarantool.org> 1.0.0
- Initial version of the RPM spec
