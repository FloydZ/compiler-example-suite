set(CMAKE_C_COMPILER ${CLANG_OPENMPOFFLOADING_CXX_COMPILER})
add_executable(clang_openmpcuda_test_datatransfer dataTransRate.c check1ns.c)
target_compile_options(clang_openmpcuda_test_datatransfer PUBLIC "-Wall -O2 -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda -I. -Xopenmp-target -march=sm_61 ")
set(CMAKE_C_COMPILER ${NATIVE_C_COMPILER})