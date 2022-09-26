project(mpi_test_project)

set(CMAKE_C_COMPILER ${MPI_C_COMPILER})
add_executable(mpitest ../src/mpitest.c)
set(CMAKE_C_COMPILER ${NATIVE_C_COMPILER})
