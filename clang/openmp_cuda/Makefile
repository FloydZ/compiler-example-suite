CC=/home/floyd.zweydinger/Downloads/llvm_build/bin/clang
dataTransRate: dataTransRate.c
	${CC} -o dataTransRate dataTransRate.c check1ns.c -Wall -O2 -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda -I. -I/opt/cuda/include  -Xopenmp-target -march=sm_61 

dataTransRate_cuda10: dataTransRate.c
	${CC} -o dataTransRate dataTransRate.c check1ns.c –-cuda-path=/opt/cuda-10.1 -Wall -O2 -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda -I. -I/opt/cuda-10.1/include -Xopenmp-target -march=sm_61
