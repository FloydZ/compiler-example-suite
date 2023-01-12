CC=clang
CPP=clang++
LD=ld

JLM=~/Downloads/compiler/jlm/bin/jlc

mptestload_nomp: 
	${CC} -o mptestload ../src/mptestload_nomp.c -O3 

jlm_mptestload_nomp:
	PATH=~/Downloads/compiler/jlm/bin/:$PATH ${JLM} -o jlm_mptestload ../src/mptestload_nomp.c -O3

mptestload: 
	${CC} -o mptestload ../src/mptestload.c -lomp  -O3 

jlm_mptestload:
	PATH=~/Downloads/compiler/jlm/bin/:$PATH ${JLM} -o jlm_mptestload ../src/mptestload.c -lomp  -O3

bitonicsort: 
	${CC} -o bitonicsort ../src/bitonicsort.cpp -O3

jlm_bitonicsort:
	PATH=~/Downloads/compiler/jlm/bin/:$PATH ${JLM} -o jlm_bitonicsort ../src/bitonicsort.cpp -O3


compare_mptestload: mptestload jlm_mptestload
	hyperfine -i ./mptestload ./jlm_mptestload
	
compare_bitonicsort: bitonicsort jlm_bitonicsort
	hyperfine -i ./bitonicsort ./jlm_bitonicsort

compare_mptestload_nomp: mptestload_nomp jlm_mptestload_nomp
	hyperfine -i ./mptestload ./jlm_mptestload
clean:
	rm -f mptestload bitonicsort jlm_bitonicsort jlm_mptestload
