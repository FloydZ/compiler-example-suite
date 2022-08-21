cmake_minimum_required (VERSION 3.9.0)
project (QSORT)

add_library(qsortlib qsort.c)
add_executable(qsortc qsort.c)
add_executable(qsortc++ qsort.cpp)
