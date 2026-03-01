cmake_minimum_required(VERSION 3.24)

include(${RP_SPLIT_LIST})
if(NOT DEFINED SPLIT_LIST)
    message(FATAL_ERROR "${RP_SPLIT_LIST} was not generated properly.")
endif()

include(${CMAKE_SOURCE_DIR}/project/Global.cmake)

#add_subdirectory(lib/sead)
#add_subdirectory(lib/NintendoWare)

project(RedPepper C CXX ASM)

#file(GLOB_RECURSE SOURCES_GAME ${CMAKE_SOURCE_DIR}/Game/src/*.c ${CMAKE_SOURCE_DIR}/Game/src/*.cpp)
#file(GLOB_RECURSE SOURCES_AL ${CMAKE_SOURCE_DIR}/lib/al/src/*.c ${CMAKE_SOURCE_DIR}/lib/al/src/*.cpp)

add_executable(RedPepper
    #$<TARGET_OBJECTS:crt0>
    ${SPLIT_LIST} ${SOURCES_GAME} ${SOURCES_AL})

set_target_properties(RedPepper PROPERTIES LINKER_LANGUAGE CXX)

#target_link_libraries(RedPepper PUBLIC sead)
#target_link_libraries(RedPepper PUBLIC nw)

target_link_options(RedPepper PRIVATE
    --startup=__ctr_start --entry=__ctr_start --keep=nnMain
    --scatter=${CMAKE_CURRENT_BINARY_DIR}/linker.ld)

#target_include_directories(RedPepper PUBLIC Game/include)
#target_include_directories(RedPepper PUBLIC lib/al/include)

