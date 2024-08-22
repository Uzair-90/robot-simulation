# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mobile_robot_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mobile_robot_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mobile_robot_FOUND FALSE)
  elseif(NOT mobile_robot_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mobile_robot_FOUND FALSE)
  endif()
  return()
endif()
set(_mobile_robot_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mobile_robot_FIND_QUIETLY)
  message(STATUS "Found mobile_robot: 0.0.0 (${mobile_robot_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mobile_robot' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mobile_robot_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mobile_robot_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mobile_robot_DIR}/${_extra}")
endforeach()
