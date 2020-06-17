^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package nextage_moveit_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.6 (2020-06-17)
------------------
* Merge pull request `#372 <https://github.com/tork-a/rtmros_nextage/issues/372>`_ from pazeshun/fix-travis
  Fix travis by fixing rosdep and moveit test
* Change target pose in moveit test to pass kinetic test
* Contributors: Kei Okada, Shun Hasegawa

0.8.5 (2019-05-10)
------------------

0.8.4 (2018-01-16)
------------------
* add moveit_armarker.rviz (`#356 <https://github.com/tork-a/rtmros_nextage/issues/356>`_)
* Contributors: Yosuke Yamamoto

0.8.3 (2017-12-22)
------------------

0.8.1 (2017-09-28)
------------------
* Add files for manuals and tutorials / Changes for Gazebo head camera emulation (`#350 <https://github.com/tork-a/rtmros_nextage/issues/350>`_)
  * move ar marker model files to nextage_gazebo/models from nextage_moveit_config/models
  * add nextage_moveit_confin/models with stl/dae/scene models and ar marker box model
  * mod name CAMERA_HEAD_R/L, remove CATKIN_IGNORE (forgot to add/rm them)
  * Merge branch 'impr/gazebo_ueye_fixtest' of git://github.com/130s/rtmros_nextage into gazebo_ueye_fixtest
  * [TEMP] Disable build on some pkgs for debugging purpose only. This MUST be reverted.
* Contributors: Isaac I.Y. Saito, Kei Okada, Yosuke Yamamoto

0.8.0 (2017-09-07)
------------------
* Fix for kinetic (`#347 <https://github.com/tork-a/rtmros_nextage/issues/347>`_)
  *  fix .travis.yaml to run both indigo/kinetic with docker
  * set trajectory_execution/allowed_execution_duration_scaling to 2.0, see https://answers.ros.org/question/196586/how-do-i-disable-execution_duration_monitoring/
  * config/NextageOpen.srdf and test/test_moveit.py: including torso to botharms is not working
  * increase set_planning_time to 30
  * run mvgroup.go() 3 time in test/test_moveit.py (test_planandexecute)
  * nextage_moveit_config/test/test_moveit.py: display content of plan
  * add replanning and set_planning_time to 15
  * increase wait_time for hztest move_group/status
  * we need type: FollowJointTrajecory in controllers.yaml
  * use move_group/MoveGroupExecuteTrajectoryAction instaeed of move_group/MoveGroupExecuteService
  * use moveit_simple_controller_manager/MoveItSimpleControllerManager instead of pr2_moveit_controller_manager/Pr2MoveItControllerManager

* Contributors: Kei Okada

0.7.16 (2017-05-04)
-------------------

0.7.15 (2017-03-11)
-------------------
* test_move_group/hztest time-limit 60->12, retry 3
* 0.7.15
* changelog for 0.7.15.
* Contributors: Isaac I.Y. Saito, Kei Okada

0.7.14 (2017-02-21)
-------------------
* [Maintenance] Enable tests for track_ik.
* Contributors: Isaac I.Y. Saito

0.7.13 (2017-01-24)
-------------------
* [capability] Add config for trac_ik.
* Contributors: Isaac I.Y. Saito

0.7.12 (2017-01-10)
-------------------

0.7.11 (2016-11-05)
-------------------

0.7.10 (2016-10-19)
-------------------
* [improve] moderate Interactive Marker size.
* Contributors: Isaac I.Y. Saito

0.7.9 (2016-10-13)
------------------
* [fix] test_moveit.py is very unstalble, run go 3 times
* [fix] NextageROS.desktop.in : now rtmlaunch is installed in global bin
* [fix][test] Better utilization of tests. test/test_moveit.py : botharms.go is very unstable
* [fix][joy.test] fix again, it seems they did not publish joint state publisher, so question is why it passed the test?
* [fix] remove torso from group, that outputs "Group 'torso' is not a chain" ERROR
* [fix] kinematics_ikfast.yaml : no ik fast plugin for head and torso
* Contributors: Kei Okada

0.7.8 (2016-07-01)
------------------
* [feat] Add joystick launch (https://groups.google.com/d/msg/moveit-users/lbUwNqiMuP8/DZX2Fn0EAQAJ).
* Contributors: Kei Okada, Isaac I.Y. Saito

0.7.7 (2016-05-16)
------------------

0.7.6 (2016-02-09)
------------------
* [fix] Use RRT as default planner (workaround/fix `#170 <https://github.com/tork-a/rtmros_nextage/issues/170>`_)
* Contributors: Isaac I.Y. Saito

0.7.5 (2016-01-27)
------------------

0.7.4 (2016-01-26)
------------------

0.7.3 (2015-12-31)
------------------
* [fix] Unnecessarily complicated dependency
* [test] Add simple tests for MoveIt
* [sys] Minor dependency update
* [doc] Fix wrong URL
* Contributors: Isaac I.Y. Saito, Kei Okada

0.7.2 (2015-11-02)
------------------

0.7.1 (2015-10-26)
------------------
* [feat] Add torso to botharm Move Group (address `#198 <https://github.com/tork-a/rtmros_nextage/issues/198>`_)
* Contributors: Isaac I.Y. Saito

0.6.6 (2015-10-17)
------------------
* [feat] Add torso, head, and (whole) upperbody Move Group
* [fix] Correct param file names for OMPL
* Contributors: Isaac I.Y. Saito

0.6.5 (2015-10-16)
------------------

0.6.4 (2015-10-02)
------------------
* [feat] Add IKFast plugin. Kinematics solver is now selectable in Moveit launch
* Contributors: Isaac IY Saito

0.6.3 (2015-08-15)
------------------
* [feat] Add `botharms`' MoveIt! group.
* Contributors: Isaac IY Saito

0.6.2 (2015-05-12)
------------------

0.6.1 (2015-03-09)
------------------

0.6.0 (2015-02-03)
------------------
* Remove non-existent eef groups.
* Contributors: Isaac IY Saito

0.5.3 (2014-11-13)
------------------

0.5.2 (2014-11-03)
------------------

0.5.1 (2014-10-17)
------------------

0.4.2 (2014-10-01)
------------------

0.4.1 (2014-09-03)
------------------
* Remove WAIST_Link to use only WAIST (Fix `#97 <https://github.com/tork-a/rtmros_nextage/issues/97>`_).
* Contributors: Isaac IY Saito

0.2.18 (2014-08-01)
-------------------
* (moveit_config) Default speed now moderately slow.
* Contributors: Isaac IY Saito

0.2.17 (2014-07-24)
-------------------

0.2.16 (2014-07-24)
-------------------
* (moveit_rviz) Correct fixed frame. This re-enables Interactive Marker to appear.
* (nextage_moveit_config) Add run_depend on hironx_moveit config (needed after https://github.com/tork-a/rtmros_nextage/commit/aa1c453c4ade5b9f44f94984f270a73e8e8e9376).
* Contributors: Isaac IY Saito

0.2.15 (2014-07-13)
-------------------
* Enable natto-view.
* Contributors: Isaac IY Saito

0.2.14 (2014-06-20)
-------------------
* Alphabetically ordering dependency
* Fix (`#73 <https://github.com/tork-a/rtmros_nextage/issues/73>`_)
* add more run_depends (`#71 <https://github.com/tork-a/rtmros_nextage/issues/71>`_)
* Contributors: Kei Okada, Isaac IY Saito

0.2.13 (2014-05-28)
-------------------
* Fix `#15 <https://github.com/tork-a/rtmros_nextage/issues/15>`_
* Contributors: Isaac IY Saito

0.2.12 (2014-05-06)
-------------------

0.2.11 (2014-03-05)
-------------------
* Fix `#23 <https://github.com/tork-a/rtmros_nextage/issues/23>`_, `#46 <https://github.com/tork-a/rtmros_nextage/issues/46>`_
* Contributors: Isaac Isao Saito

0.2.10 (2014-02-18)
-------------------

0.2.9 (2014-02-03)
------------------

0.2.8 (2014-02-03)
------------------

0.2.7 (2014-01-19)
------------------

0.2.6 (2014-01-13)
------------------

0.2.5 (2013-12-25)
------------------

0.2.4 (2013-12-03)
------------------

0.2.3 (2013-11-05)
-----------

0.2.2 (2013-11-04)
-----------
* nextage_moveit_config) arm speed faster
* nextage_moveit_config) disable mongodb
* Adjust to web-tablet version discussed at https://github.com/start-jsk/open-industrial-controllers/issues/121. Please revert this if this causes any bad effect.
* nextage_moveit_config) increase velocity and acceleration

0.2.1 (2013-10-31)
------------------
* Initial commit to the public repo (migrated from private repo)
