CC=~/Downloads/compiler/llvm_build/bin/clang
CPP=~/Downloads/compiler/llvm_build/bin/clang++

axpy: axpy.cu
	${CPP} -o axpy axpy.cu --cuda-path=/opt/cuda --cuda-gpu-arch=sm_35  -L/opt/cuda/lib64 -ldl -lrt -pthread
