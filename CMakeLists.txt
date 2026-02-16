cmake_minimum_required(VERSION 3.24)

set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/project/ARMCC.cmake)
include(${CMAKE_SOURCE_DIR}/project/Global.cmake)
set_toolchain()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_subdirectory(lib/sead)
add_subdirectory(lib/NintendoWare)

project(RedPepper C CXX ASM)

set(CMAKE_EXECUTABLE_SUFFIX ".axf")

__compiler_armcc(C)
__compiler_armcc(CXX)
__compiler_armcc(ASM)

file(GLOB_RECURSE SOURCES_GAME ${CMAKE_SOURCE_DIR}/Game/src/*.c ${CMAKE_SOURCE_DIR}/Game/src/*.cpp)
file(GLOB_RECURSE SOURCES_AL ${CMAKE_SOURCE_DIR}/lib/al/src/*.c ${CMAKE_SOURCE_DIR}/lib/al/src/*.cpp)

add_executable(RedPepper $<TARGET_OBJECTS:crt0> ${CMAKE_BINARY_DIR}/split/orig.o ${SOURCES_GAME} ${SOURCES_AL})

target_link_libraries(RedPepper PUBLIC sead)
target_link_libraries(RedPepper PUBLIC nw)

target_link_options(RedPepper PRIVATE
    --entry=__ctr_start --startup=__ctr_start
    --library_type=standardlib --no_remove --datacompressor=off
    --legacyalign --tailreorder --inline # no_remove to keep the unreferenced
    --verbose --mangled --symbols --paged
    --scatter=${CMAKE_CURRENT_BINARY_DIR}/linker.ld
    )

target_include_directories(RedPepper PUBLIC Game/include)
target_include_directories(RedPepper PUBLIC lib/al/include)

