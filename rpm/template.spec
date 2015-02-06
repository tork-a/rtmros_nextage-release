Name:           ros-hydro-nextage-description
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS nextage_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nextage_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-urdf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-urdf

%description
As a part of rtmros_nextage package that is a ROS interface for Nextage dual-
armed robot from Kawada Robotics Inc, this package provides its 3D model that
can be used in simulation and MoveIt!-based motion planning tasks.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.6.0-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.5.3-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.5.2-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.5.1-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.4.2-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.4.1-0
- Autogenerated by Bloom

* Fri Aug 01 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.18-0
- Autogenerated by Bloom

