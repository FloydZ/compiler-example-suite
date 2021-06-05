/******************************************************************************
* FILE: mptestload2.c
* DESCRIPTION:
*   OpenMP Example - Sections Work-sharing - C Version
*   In this example, threads work in parallel on the same datastructure via the 
*	parallel for simd construction. Additoinally the aligned and safelen primitves
*	are used.
*	See: https://bisqwit.iki.fi/story/howto/openmp/
* AUTHOR: Floyd Zweydinger 05.06.21
* Compile it with: `gcc -Ofast -fopenmp mptestload3.c -o test`
******************************************************************************/
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>

#define N     500000
const uint32_t THREADS = 2;
const uint64_t NT = N/THREADS;

int main (int argc, char *argv[])  {
	omp_set_num_threads(THREADS);
	
	float a[N], b[N], c[N], d[N];

	// Some initializations
	for (uint64_t i=0; i<N; i++) {
	  a[i] = i * 1.5;
	  b[i] = i + 22.35;
	  c[i] = d[i] = 0.0;
	}

	#pragma omp parallel for simd aligned(a,b,c:16) safelen(4)
	for (uint64_t i=0; i<N; i++) {
		c[i] = a[i] + b[i];
		printf("Thread %d: c[%d]= %f\n",omp_get_thread_num(),i,c[i]);
	}

	#pragma omp parallel for simd aligned(a,b,d:16) safelen(4)
	for (uint64_t i=0; i<N; i++) {
		d[i] = a[i] * b[i];
		printf("Thread %d: d[%d]= %f\n",omp_get_thread_num(),i,d[i]);
	}

	assert(d[NT-1] == 93757628416.000000);
}
