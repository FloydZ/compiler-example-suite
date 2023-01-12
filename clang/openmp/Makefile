CC=clang
CPP=clang++
OPT=opt

# good src: https://llvm.org/devmtg/2020-09/slides/PGO_Instrumentation.pdf
mptestload:
	clang -o mptestload ../../src/mptestload.c -lomp -O3 -march=native -fprofile-instr-generate
	LLVM_PROFILE_FILE="code-%p.profraw" ./mptestload
	llvm-profdata merge -output=code.profdata code-*.profraw
	clang -o mptestload ../../src/mptestload.c -lomp -O3 -march=native -fprofile-instr-use=code.profdata -fdiagnostics-show-hotness -fdiagnostics-fixit-info -fsave-optimization-record  -foptimization-record-file=test.txt -Rpass -Rpass-missed -Rpass-analysis -o mptestload_f

clean:
	rm mptestload
