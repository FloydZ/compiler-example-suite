set(CMAKE_CUDA_COMPILER ${CLANG_CUDA_CXX_COMPILER})
add_executable(clang_cuda_test_axpy axpy.cu)
add_executable(clang_cuda_test_cudatest cudatest.cu)
#TODO flags
set(CMAKE_CUDA_COMPILER ${NATIVE_CUDA_COMPILER})