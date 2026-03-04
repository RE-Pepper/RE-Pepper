cmake_minimum_required(VERSION 3.24)

if(NOT DEFINED RP_SPLIT_LIST)
    message(FATAL_ERROR "Please run the project from the tools/build.py file.")
endif()
include(${RP_SPLIT_LIST})
if(NOT DEFINED SPLIT_LIST)
    message(FATAL_ERROR "${RP_SPLIT_LIST} was not generated properly.")
endif()

include(${CMAKE_SOURCE_DIR}/project/Global.cmake)

#add_subdirectory(lib/sead)
#add_subdirectory(lib/NintendoWare)

# Splector

add_library(SplectorO OBJECT ${SPLIT_LIST})

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Splector.elf
    COMMAND armlink --partial
        $<JOIN:$<TARGET_OBJECTS:SplectorO>, >
        -o ${CMAKE_CURRENT_BINARY_DIR}/Splector.elf
    DEPENDS $<TARGET_OBJECTS:SplectorO>)

add_custom_target(Splector DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/Splector.elf)

# RedPepper

project(RedPepper C CXX ASM)

#file(GLOB_RECURSE SOURCES_GAME ${CMAKE_SOURCE_DIR}/Game/src/*.c ${CMAKE_SOURCE_DIR}/Game/src/*.cpp)
#file(GLOB_RECURSE SOURCES_AL ${CMAKE_SOURCE_DIR}/lib/al/src/*.c ${CMAKE_SOURCE_DIR}/lib/al/src/*.cpp)

add_executable(RedPepper
    #$<TARGET_OBJECTS:crt0>
    ${CMAKE_CURRENT_BINARY_DIR}/Splector.elf
    Game/src/Stubs.c
    ${SOURCES_GAME} ${SOURCES_AL})

set_source_files_properties(${CMAKE_CURRENT_BINARY_DIR}/Splector.elf PROPERTIES GENERATED TRUE)
add_dependencies(RedPepper
    #crt0
    Splector)

set_target_properties(RedPepper PROPERTIES LINKER_LANGUAGE CXX)

#target_link_libraries(RedPepper PRIVATE sead)
#target_link_libraries(RedPepper PRIVATE nw)

target_link_options(RedPepper PRIVATE
    --startup=__ctr_start --entry=__ctr_start --keep=nnMain
    --scatter=${CMAKE_CURRENT_BINARY_DIR}/linker.ld)

target_include_directories(RedPepper PUBLIC Game/include)
target_include_directories(RedPepper PUBLIC lib/al/include)

