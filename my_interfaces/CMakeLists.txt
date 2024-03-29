cmake_minimum_required(VERSION 3.5)
project(my_interfaces)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)  # 추가
find_package(builtin_interfaces REQUIRED)  # 추가
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
set(topicfile
  "msg/ArithmeticArgument.msg"
)

set(servicefile
  "srv/TwoIntAdd.srv"
  "srv/ArithmeticOperator.srv"
)

set(actionfile
  "action/Fibonacci.action"
  "action/ArithmeticChecker.action"
)

rosidl_generate_interfaces(     # 추가
  ${PROJECT_NAME}
  ${topicfile}
  ${servicefile}  
  ${actionfile}  
)

# add_executable()
# install()


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_dependencies(rosidl_default_runtime)  # 추가
ament_package()
