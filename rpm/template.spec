Name:           ros-kinetic-nextage-ros-bridge
Version:        0.8.2
Release:        0%{?dist}
Summary:        ROS nextage_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nextage_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-hironx-ros-bridge >= 1.1.13
Requires:       ros-kinetic-nextage-description
Requires:       ros-kinetic-stereo-image-proc
Requires:       ros-kinetic-ueye-cam
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-hironx-ros-bridge >= 1.1.13
BuildRequires:  ros-kinetic-nextage-description
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rostest

%description
A main ROS interface for developers and users of Nextage dual-armed robot from
Kawada Robotics Inc. Developers can build their own application that takes
control over Nextage via this package. Interface for both ROS and OpenRTM is
provided.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Sep 28 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.2-0
- Autogenerated by Bloom

* Thu Sep 07 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.0-0
- Autogenerated by Bloom

