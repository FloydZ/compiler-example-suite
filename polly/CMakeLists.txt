cmake_minimum_required(VERSION 3.20.1)
project(pollybolt)

set(CMAKE_C_STANDARD 11)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_VERBOSE_MAKEFILE ON)

add_executable(mptestload mptestload.c)
target_compile_options(mptestload PUBLIC -fopenmp -O3)
target_link_libraries(mptestload omp)

add_executable(mptestload_polly mptestload.c)
target_compile_options(mptestload_polly PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	)
target_link_libraries(mptestload_polly omp)


add_executable(mptestload_polly_scheduler_static mptestload.c)
target_compile_options(mptestload_polly_scheduler_static PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	"SHELL:-mllvm -polly-scheduling=static"
	)
target_link_libraries(mptestload_polly_scheduler_static omp)

add_executable(mptestload_polly_scheduler_dynamic mptestload.c)
target_compile_options(mptestload_polly_scheduler_dynamic PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	"SHELL:-mllvm -polly-scheduling=dynamic"
	)
target_link_libraries(mptestload_polly_scheduler_dynamic omp)

add_executable(mptestload_polly_scheduler_guided mptestload.c)
target_compile_options(mptestload_polly_scheduler_guided PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	"SHELL:-mllvm -polly-scheduling=guided"
	)
target_link_libraries(mptestload_polly_scheduler_guided omp)


add_executable(mptestload_polly_LLVM mptestload.c)
target_compile_options(mptestload_polly_LLVM PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	"SHELL:-mllvm -polly-omp-backend=LLVM"
	)
target_link_libraries(mptestload_polly_LLVM omp)


add_executable(mptestload_polly_vector mptestload.c)
target_compile_options(mptestload_polly_vector PRIVATE 
	-O3 
	"SHELL:-mllvm -polly"
	"SHELL:-mllvm -polly-parallel"
	"SHELL:-mllvm -polly-num-threads=4"
	"SHELL:-mllvm -polly-vectorizer=stripmine"
	)
target_link_libraries(mptestload_polly_vector omp)


#add_executable(mptestload_polly_simplify mptestload.c)
#target_compile_options(mptestload_polly_simplify PRIVATE 
#	-O3 
#	"SHELL:-mllvm -polly"
#	"SHELL:-mllvm -polly-parallel"
#	"SHELL:-mllvm -polly-num-threads=4"
#	"SHELL:-mllvm -polly-simplify"
#	)
#target_link_libraries(mptestload_polly_simplify omp)
