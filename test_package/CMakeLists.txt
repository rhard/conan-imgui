project(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(OpenGL REQUIRED)
include_directories(../imgui/examples/libs/gl3w)

file(GLOB OPENGL3_SRC "../imgui/examples/opengl3_example/*.cpp")

add_executable(opengl3_example  ../imgui/examples/libs/gl3w/GL/gl3w.c ../imgui/imgui_demo.cpp ${OPENGL3_SRC})
target_link_libraries(opengl3_example ${CONAN_LIBS} opengl32)
