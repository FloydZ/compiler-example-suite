set(CMAKE_C_COMPILER ${CLANG_POLLY_C_COMPILER})
set(CMAKE_CXX_COMPILER ${CLANG_POLLY_CXX_COMPILER})

add_executable(clang_polly_test_mptest mptest.c)
add_executable(clang_polly_test_mptestload mptestload.c)
target_compile_options(clang_polly_test_mptestload PUBLIC -O3 -mllvm -polly -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-num-threads=4 -lomp)


set(CMAKE_C_COMPILER ${NATIVE_C_COMPILER})
set(CMAKE_CXX_COMPILER ${NATIVE_CXX_COMPILER})