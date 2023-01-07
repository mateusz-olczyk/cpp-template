include_guard()

function(myproject_target_add_warnings TARGET)
    if(MYPROJECT_WITH_EXTRA_WARNINGS)
        target_compile_options(${TARGET} PRIVATE
            $<$<CXX_COMPILER_ID:Clang,GNU>:-Wall
                                           -Wextra
                                           -Wmissing-declarations
                                           -Wsign-conversion
                                           -Wpedantic
                                           -Wshadow>
            $<$<CXX_COMPILER_ID:MSVC>:/W4>
        )
    endif()
endfunction()

function(myproject_target_setup_clangformat TARGET)
    if(MYPROJECT_WITH_CLANGFORMAT)
        include(ClangFormat)
        target_clangformat_setup(${TARGET})
    endif()
endfunction()

function(myproject_includedirs_setup_clangformat)
    if(MYPROJECT_WITH_CLANGFORMAT)
        include(ClangFormat)
        foreach(HEADER_DIRECTORY IN LISTS ARGN)
            file(GLOB HEADER_DIRECTORY_HEADERS "${HEADER_DIRECTORY}/*.hpp")
            list(APPEND ALL_HEADERS ${HEADER_DIRECTORY_HEADERS})
        endforeach()
        clangformat_setup(${ALL_HEADERS})
    endif()
endfunction()
