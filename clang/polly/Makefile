CC=/home/floyd.zweydinger/Downloads/llvm_build/bin/clang
CPP=/home/floyd.zweydinger/Downloads/llvm_build/bin/clang++
OPT=/home/floyd.zweydinger/Downloads/llvm_build/bin/opt

polly_mptest: mptest.c
	${CC} -o mptest mptest.c -O3 -mllvm -polly -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-num-threads=4  -mllvm -polly-dump-before-file=before-polly.ll -lgomp

polly_mptestload: mptestload.c
	${CC} -o mptestload mptestload.c -O3 -mllvm -polly -mllvm -polly-parallel -mllvm -polly-omp-backend=LLVM -mllvm -polly-num-threads=4 -lomp

# this approach is LLVM old way into passing different optimisation flags to polly. It creates an Object file.
# the 2. command shows all commands passed to the optimizer.
polly_mptestload_with_opt: mptestload.c
	${CC} -o mptestload mptestload.c -O3 -mllvm -polly -mllvm -polly-dump-before-file=mptestload_before-polly.ll -lomp
	${CC} mptestload.c -c -O3 -mllvm -polly -mllvm -debug-pass=Arguments
	${OPT} --polly-simplify --polly-optree --polly-delicm --polly-simplify --polly-prune-unprofitable --polly-opt-isl --polly-codegen  mptestload_before-polly.ll > opt_mptestload.o
