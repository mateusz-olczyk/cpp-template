cmake_minimum_required(VERSION 3.16)
project(MyProject DESCRIPTION "My project description" LANGUAGES CXX)

option(MYPROJECT_WITH_EXTRA_WARNINGS "Enable extra compilation warnings" ON)
option(MYPROJECT_WITH_TESTS "Enable unit and integration tests" OFF)
option(MYPROJECT_WITH_CLANGFORMAT "Add 'clangformat' custom target which runs clang-format on all sources" OFF)

# ------------------------------------------------------------------------------

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# ------------------------------------------------------------------------------

add_subdirectory(src)

if(MYPROJECT_WITH_TESTS)
    enable_testing()
    add_subdirectory(test)
endif()
