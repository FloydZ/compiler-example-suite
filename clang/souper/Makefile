CC=clang
SCLANG=/home/duda/Downloads/souper/build/sclang
PASS=/home/duda/Downloads/souper/build/libsouperPass.so

mptestload: mptestload.c
	${CC} -o mptestload mptestload.c -O3 -lomp

sclang_mptestload: mptestload.c
	${SCLANG} -o sclang_mptestload mptestload.c -O3 -lomp

souper_mptestload: mptestload.c
	${CC} -o mptestload mptestload.c -O3  -Xclang -load -Xclang ${PASS} -mllvm -z3-path=/usr/bin/z3 -lomp
