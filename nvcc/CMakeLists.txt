cmake_minimum_required(VERSION 3.10)
project(cuda_test_project CUDA)

set(CUDA_ARCHITECTURE sm_60)
add_executable(cuda_test ../src/cuda/cudatest.cu)
