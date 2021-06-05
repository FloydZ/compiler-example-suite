/******************************************************************************
* FILE: mptestload2.c
* DESCRIPTION:
*   OpenMP Example - Sections Work-sharing - C Version
*   In this example, threads work in parallel on the same datastructure. 
* AUTHOR: Floyd Zweydinger 05.06.21
* Compile it with: `gcc -Ofast -fopenmp mptestload2.c -o test`
******************************************************************************/
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

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

#pragma omp parallel shared(a,b,c,d)
	{
		int tid = omp_get_thread_num();
		
		uint64_t start 	= tid*NT;
		uint64_t end 	= (tid+1)*NT;
		
		if (tid == 0) {
			int nthreads = omp_get_num_threads();
			printf("Number of threads = %d\n", nthreads);
		}
		
		printf("Thread %d starting...\n",tid);

		{
			// printf("Thread %d doing section 1\n",tid);
			for (uint64_t i=start; i<end; i++) {
				c[i] = a[i] + b[i];
				printf("Thread %d: c[%d]= %f\n",tid,i,c[i]);
			}
		}


		{
			// printf("Thread %d doing section 2\n",tid);
			for (uint64_t i=start; i<end; i++) {
				d[i] = a[i] * b[i];
				printf("Thread %d: d[%d]= %f\n",tid,i,d[i]);
			}

		}

		printf("Thread %d done.\n",tid); 

	}

}
