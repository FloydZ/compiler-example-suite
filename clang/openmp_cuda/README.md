# Introduction

The directories in this repository contain code examples for the course of
OpenMP GPU-offloading at Paderborn Center for Parallel Computing (PC²),
Paderborn University. The sub-directories are generally organized as:

* src: source code
* docs: documentation
* tests: some tests

Some highlights of the codes in this repository:

* The performance of our `saxpy` implemented by using OpenMP GPU-offloading is
  as good as `cublasSaxpy` in CUBLAS. See `case 7` in `05_saxpy/src/asaxpy.c`
  for details.

* The GPU shared memory has not been standardized in OpenMP API Specification
  (Version 5.0 Nov. 2018). To optimize the performance of matrix multiplication
  by using OpenMP GPU-offloading, i) `case 6` in `10_matMul/src/matMulAB.c`
  implements a register blocking algorithm and ii) `case 8` in the same source
  code file implements a common GPU-based tiled algorithm by blocking the local
  shared memory in a very tricky manner and the OpenMP code resembles CUDA.

# List of Projects

* 00_build_OpenMP_offload

  Documentation and scripts for building GCC as well as Clang/LLVM with OpenMP
  support for Nvidia GPU offloading.

* 01_accelQuery

  `accelQuery` searches accelerator(s) on a heterogeneous computer.
  Accelerator(s), if found, will be enumerated with some basic info.

* 02_dataTransRate

  `dataTransRate` gives the data transfer rate (in MB/sec) from `src` to `dst`.

  The possible situations are:

  * h2h: `src` = host  and `dst` = host
  * h2a: `src` = host  and `dst` = accel
  * a2a: `src` = accel and `dst` = accel

  NOTE:

  * A bug in Clang 9.0.1 has been fixed in Clang 11.
  * The data transfer rata for `a2a` is still lower than our expectation.

* 03_taskwait

  `taskwait` checks the `taskwait` construct for the deferred target task.

  NOTE:

  * Asynchronous offloading hasn't been implemented in the GCC 9.2 compiler.
  * Asynchronous offloading is available in Clang 11.

* 04_scalarAddition

  `scalarAddition` adds two integers on host and accelerator, and also compares
  the performance.

* 05_saxpy

  `saxpy` performs the `saxpy` operation on host as well as accelerator.
  The performance (in MB/s) for different implementations is also compared.

* 08_distThreads

  `distThreads` demonstrates the organization of threads and teams in a league
  on GPU.

* 09_matAdd

  `matAdd` performs matrix addition (A +=B) in single-precision on GPU. The
  performance (in GB/s) for different implementations is compared and the
  numerical results are also verified.

* 10_matMul

  `matMul` performs matrix multiplication in single-precision on GPU. The
  performance (in GFLOPS) for different implementations is compared and the
  numerical results are also verified.
