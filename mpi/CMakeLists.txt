set(CMAKE_C_COMPILER ${MPI_C_COMPILER})
add_executable(mpitest mpitest.c)
set(CMAKE_C_COMPILER ${NATIVE_C_COMPILER})
