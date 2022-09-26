CC=clang
CPP=clang++
LD=ld

PERF2BOLT=~/Downloads/compiler/bolt/build/bin/perf2bolt
BOLT=~/Downloads/compiler/bolt/build/bin/llvm-bolt

mptestload: 
	${CC} -o mptestload ../../src/mptestload.c -lomp  -O3 -march=native

bolt_mptestload: mptestload
	${CC} -o mptestload.reloc ../../src/mptestload.c -O3 -march=native -lstdc++ -lomp -Xlinker --emit-relocs
	perf record -e cycles:u -j any,u -o perf.data -- ./mptestload.reloc
	# or
	# llvm-bolt mptestload -instrument -o mptestload.reloc
	# ./mptestload.reloc
	${PERF2BOLT} -p perf.data -o perf.fdata mptestload.reloc
	${BOLT} mptestload.reloc -o mptestload.bolt -data=perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats


bitonicsort: 
	${CC} -o bitonicsort ../../src/bitonicsort.cpp -lomp  -lstdc++ -O3 -march=native

bolt_bitonicsort: bitonicsort
	${CC} -o bitonicsort.reloc ../../src/bitonicsort.cpp -O3 -march=native -lomp -lstdc++ -Xlinker --emit-relocs
	perf record -e cycles:u -j any,u -o perf.data -- ./bitonicsort.reloc
	# or
	# llvm-bolt bitonicsort -instrument -o bitonicsort.reloc
	# ./bitonicsort.reloc
	${PERF2BOLT} -p perf.data -o perf.fdata bitonicsort.reloc
	${BOLT} bitonicsort.reloc -o bitonicsort.bolt -data=perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats


compare_mptestload: mptestload bolt_mptestload
	hyperfine ./mptestload ./mptestload.bolt
	
compare_bitonicsort: bitonicsort bolt_bitonicsort
	hyperfine ./bitonicsort ./bitonicsort.bolt
