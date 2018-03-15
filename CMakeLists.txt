cmake_minimum_required(VERSION 3.9)
project(imgui)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup()
else()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

set(CMAKE_CXX_STANDARD 11)

include_directories(imgui)

add_library(imgui imgui/imgui.cpp imgui/imgui_draw.cpp)