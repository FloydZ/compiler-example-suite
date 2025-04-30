cmake_minimum_required(VERSION 3.15)
project(test C)

set(CMAKE_C_STANDARD 17)
SET(CMAKE_VERBOSE_MAKEFILE true)

include_directories(src)

add_executable(example_c example.c)
target_link_libraries(example_c -fopenmp)
