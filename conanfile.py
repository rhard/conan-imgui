from conans import ConanFile, CMake, tools
import os

class ImguiConan(ConanFile):
    name = "imgui"
    version = "1.53"
    license = "MIT"
    url = "https://github.com/rhard/conan-imgui"
    description = "Dear ImGui is a bloat-free graphical user interface library for C++."
    settings = "os", "compiler", "build_type", "arch"
    sources_folder = "source_subfolder"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"

    def source(self):
        zipname = 'v1.53.tar.gz'
        url = 'https://github.com/ocornut/imgui/archive/%s' % zipname
        tools.download(url, zipname)
        tools.unzip(zipname)
        os.unlink(zipname)
        os.rename("imgui-1.53", self.sources_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="License*", dst="licenses", src=self.sources_folder, ignore_case=True, keep_path=False)
        self.copy("imgui.h", dst="include", src=self.sources_folder)
        self.copy("imconfig.h", dst="include", src=self.sources_folder)
        self.copy("imgui_internal.h", dst="include", src=self.sources_folder)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["imgui"]
