
include(MyprojectUtils)

set(MYPROJECT_HEADERS_DIRS "${PROJECT_SOURCE_DIR}/include")
myproject_includedirs_setup_clangformat(${MYPROJECT_HEADERS_DIRS})

set(MYPROJECT_SOURCES
    lib.cpp
)

# ------------------------------------------------------------------------------

add_library(myproject_internals ${MYPROJECT_SOURCES})
target_include_directories(myproject_internals PUBLIC ${MYPROJECT_HEADERS_DIRS})
myproject_target_add_warnings(myproject_internals)
myproject_target_setup_clangformat(myproject_internals)

# ------------------------------------------------------------------------------

add_executable(myproject_app main.cpp)
target_link_libraries(myproject_app PRIVATE myproject_internals)
myproject_target_add_warnings(myproject_app)
myproject_target_setup_clangformat(myproject_app)
