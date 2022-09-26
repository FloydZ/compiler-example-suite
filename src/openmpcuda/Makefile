CC=/home/duda/Downloads/BOLT/build/bin/clang
CPP=/home/duda/Downloads/BOLT/build/bin/clang++ 
OMPFILE=--libomp
ARCH=-Xopenmp-target -march=sm_60

dataTransRate: dataTransRate.c
	${CC} -o dataTransRate dataTransRate.c check1ns.c -Wall -O2 -fopenmp -fopenmp-targets=nvptx64 -I.

dataTransRate_cuda10: dataTransRate.c
	${CC} -o dataTransRate dataTransRate.c check1ns.c -Wall -O2  -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda -I. -I/opt/cuda-10.1/incl$

simple: simple.cpp
	${CPP} -v -o simple simple.cpp -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda ${ARCH}

simple2: simple2.cpp
	${CPP} -v -o simple2 -fopenmp -fopenmp-targets=nvptx64-nvidia-cuda ${ARCH} -O2 simple2.cpp -lomptarget
