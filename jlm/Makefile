CC=clang
CPP=clang++
LD=ld

JLM=~/Downloads/compiler/jlm/bin/jlc

mptestload: 
	${CC} -o mptestload ../src/mptestload.c -lomp  -O3 

jlm_mptestload: mptestload
	PATH=~/Downloads/compiler/jlm/bin/:$PATH ${JLM} -o jlm_mptestload ../src/mptestload.c -lomp  -O3


bitonicsort: 
	${CC} -o bitonicsort ../src/bitonicsort.cpp -O3

jlm_bitonicsort: bitonicsort
	PATH=~/Downloads/compiler/jlm/bin/:$PATH ${JLM} -o jlm_bitonicsort ../src/bitonicsort.cpp -O3


compare_mptestload: mptestload jlm_mptestload
	hyperfine ./mptestload ./jlm_mptestload
	
compare_bitonicsort: bitonicsort jlm_bitonicsort
	hyperfine ./bitonicsort ./jlm_bitonicsort
