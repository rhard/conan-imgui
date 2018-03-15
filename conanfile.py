from conans import ConanFile, CMake, tools
import os

class ImguiConan(ConanFile):
    name = "imgui"
    version = "1.53"
    license = "https://github.com/ocornut/imgui/blob/master/LICENSE.txt"
    url = "https://github.com/rhard/conan-imgui"
    description = "Dear ImGui is a bloat-free graphical user interface library for C++."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"

    def source(self):
        if not os.path.exists(os.path.join(self.source_folder, "imgui")):
            self.run("git clone https://github.com/ocornut/imgui.git")
        self.run("cd imgui && git fetch --all --tags")
        self.run("cd imgui && git checkout tags/v%s" % self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("imgui.h", dst="include", src="imgui")
        self.copy("imconfig.h", dst="include", src="imgui")
        self.copy("imgui_internal.h", dst="include", src="imgui")
        self.copy("imgui.lib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["imgui"]
