CC= ~/Downloads/compiler/polly/build/bin/clang
CPP=~/Downloads/compiler/polly/build/bin/clang++
OPT=~/Downloads/compiler/polly/build/bin/opt

# a little useles test: `mptest` only prints its name.
polly_mptest:
	${CC} -o polly_mptest ../../src/mptest.c -O3 -mllvm -polly -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-num-threads=4  -mllvm -polly-dump-before-file=before-polly.ll -lgomp

polly_mptestload:
	${CC} -o polly_mptestload ../../src/mptestload.c -O3 -mllvm -polly -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-num-threads=4 -lomp -O3 -march=native

mptestload:
	clang -o mptestload ../../src/mptestload.c -fopenmp  -O3 -march=native -g -gdwarf-3 -gstrict-dwarf

mptestload_nomp:
	clang -o mptestload ../../src/mptestload_nomp.c -O3 -march=native -g -gdwarf-3 -gstrict-dwarf
	gcc -c -o mptestload_nomp.o ../../src/mptestload_nomp.c -O3 -march=native -g -gdwarf-3 -gstrict-dwarf -fno-stack-protector -fno-pie -fno-PIC -fno-lto
	# gcc mptestload_nomp.o -o mptestload_nomp  -fno-pie -fno-PIC
	ld mptestload_nomp.o -o mptestload_nomp

compare_mptestload: mptestload polly_mptestload
	hyperfine ./mptestload ./polly_mptestload

# this approach is LLVM old way into passing different optimisation flags to polly. It creates an Object file.
# the 2. command shows all commands passed to the optimizer.
polly_mptestload_with_opt: mptestload.c
	${CC} -o mptestload ../../src/mptestload.c -O3 -mllvm -polly -mllvm -polly-dump-before-file=mptestload_before-polly.ll -lomp
	${CC} mptestload.c -c -O3 -mllvm -polly -mllvm -debug-pass=Arguments
	${OPT} --polly-simplify --polly-optree --polly-delicm --polly-simplify --polly-prune-unprofitable --polly-opt-isl --polly-codegen  mptestload_before-polly.ll > opt_mptestload.o

clean:
	rm -f mptestload mptestload_nomp polly_mptestload
