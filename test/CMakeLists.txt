include(FetchContent)
include(GoogleTest)
include(MyprojectUtils)

set(MYPROJECT_TEST_SOURCES
    test_lib.cpp
)

# ------------------------------------------------------------------------------

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        release-1.12.1
)
FetchContent_MakeAvailable(googletest)

# ------------------------------------------------------------------------------

add_executable(myproject_test ${MYPROJECT_TEST_SOURCES})
target_link_libraries(myproject_test PRIVATE gtest_main myproject_internals)
myproject_target_add_warnings(myproject_test)
myproject_target_setup_clangformat(myproject_test)
gtest_discover_tests(myproject_test)

# ------------------------------------------------------------------------------

find_package(Valgrind)
if (Valgrind_FOUND)
    add_test(
        NAME ValgrindCheck

        COMMAND
        ${Valgrind_EXECUTABLE}
        --error-exitcode=1
        --leak-check=full
        --show-leak-kinds=all
        $<TARGET_FILE:myproject_test>
    )
endif()
