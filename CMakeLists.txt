cmake_minimum_required(VERSION 3.8)
project(first_bot)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config description launch worlds DESTINATION share/${PROJECT_NAME})

ament_package()
