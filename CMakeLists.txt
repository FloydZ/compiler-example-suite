CMAKE_MINIMUM_REQUIRED(VERSION 3.8)
project ("compiler example suite" LANGUAGES CUDA C CXX)
set(CMAKE_VERBOSE_MAKEFILE ON)

# global include path for dependencies
# maybe a little ugly, but the easiest way to include `cuda_runtime.h`
# as far as i know this is only needed for arch linux.
include_directories(/opt/cuda/samples/common/inc)
include_directories(/opt/cuda/include)

if(NOT DEFINED CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_CXX_STANDARD_REQUIRED True)
endif()

if(NOT DEFINED CMAKE_CUDA_STANDARD)
    set(CMAKE_CUDA_STANDARD 11)
    set(CMAKE_CUDA_STANDARD_REQUIRED True)
endif()

# fall back, if one does not directly have a CUDA rdy card, but rather a optimus (internal laptop) card.
if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
    set(CMAKE_CUDA_ARCHITECTURES 61)
endif()

# Set the compilers
set(MPI_C_COMPILER "mpiCC")
set(CLANG_POLLY_C_COMPILER "TODO")
set(CLANG_POLLY_CXX_COMPILER "TODO")
set(CLANG_CUDA_C_COMPILER "TODO")
set(CLANG_CUDA_CXX_COMPILER "TODO")
set(CLANG_OPENMPOFFLOADING_C_COMPILER "TODO")
set(CLANG_OPENMPOFFLOADING_CXX_COMPILER "TODO")


add_subdirectory(clang)
add_subdirectory(mpi)
add_subdirectory(nvcc)
add_subdirectory(ispc)
add_subdirectory(dpc++)