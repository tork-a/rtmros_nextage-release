Name:           ros-kinetic-nextage-calibration
Version:        0.8.3
Release:        1%{?dist}
Summary:        ROS nextage_calibration package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nextage_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-checkerboard-detector
Requires:       ros-kinetic-dynamic-tf-publisher
Requires:       ros-kinetic-freenect-stack
Requires:       ros-kinetic-gazebo-plugins
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-openni2-launch
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-turtlebot-description
Requires:       ros-kinetic-urdf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-nextage-gazebo

%description
This package provides .launch files and other tools for calibrating the head-
mount cameras to the NEXTAGE Open robot. As of version 0.7.15/March 2017, only
Kinect/Xtion is capable (i.e. Ueye cameras, the ones the robot comes with on
this head by default, are not yet handled).

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
* Tue Jan 16 2018 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.3-1
- Autogenerated by Bloom

* Fri Dec 22 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.3-0
- Autogenerated by Bloom

* Thu Sep 28 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.2-0
- Autogenerated by Bloom

* Thu Sep 07 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.8.0-0
- Autogenerated by Bloom

