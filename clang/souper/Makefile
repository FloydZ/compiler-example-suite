CC=clang
CPP=clang++
SCLANG=/home/duda/Downloads/compiler/souper/build/sclang
SCLANGPP=/home/duda/Downloads/compiler/souper/build/sclang++
PASS=/home/duda/Downloads/comiler/souper/build/libsouperPass.so
	
.PHONY : all

mptestload:
	${CC} -o mptestload ../../src/mptestload.c -O3 -lomp -march=native

bitonicsort:
	${CPP} -o bitonicsort ../../src/bitonic_sort.cpp -O3 -lomp -march=native

# comment the following line to enable redis caches
sclang_mptestload: export SOUPER_NO_EXTERNAL_CACHE=1
sclang_mptestload:
	${SCLANG} -o sclang_mptestload ../../src/mptestload.c -O3 -lomp -march=nativ

sclang_bitonicsort: export SOUPER_NO_EXTERNAL_CACHE=1
sclang_bitonicsort:
	${SCLANGPP} -o sclang_bitonicsort ../../src/bitonicsort.cpp -O3 -lomp -march=native

souper_mptestload:
	${CC} -o mptestload ../../src/mptestload.c -O3  -Xclang -load -Xclang ${PASS} -mllvm -z3-path=/usr/bin/z3 -lomp

compare_mptestload: mptestload sclang_mptestload
	hyperfine -i ./mptestload ./sclang_mptestload

compare_bitonicsort: bitonicsort sclang_bitonicsort
	hyperfine -i ./bitonicsort ./sclang_bitonicsort

all : sclang_mptestload mptestload souper_mptestload
