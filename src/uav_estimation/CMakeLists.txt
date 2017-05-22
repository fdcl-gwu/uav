cmake_minimum_required(VERSION 2.8.3)
project(estimation)
find_package(catkin REQUIRED COMPONENTS rospy)


catkin_package()
catkin_python_setup()
catkin_install_python(PROGRAMS ukf_uav/ukf_uav.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
