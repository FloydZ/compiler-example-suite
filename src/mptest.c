#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main (int argc, char *argv[]){
	int nthreads, tid;

	char hostname[1024];
	hostname[1023] = '\0';
	gethostname(hostname, 1023);
	printf("Hostname: %s\n", hostname);

	/* Fork a team of threads giving them their own copies of variables */
	#pragma omp parallel private(nthreads, tid)
  	{
  		/* Obtain thread number */
  		tid = omp_get_thread_num();
  		printf("Hello World from thread = %d\n", tid);

  		/* Only master thread does this */
  		if (tid == 0) {
    			nthreads = omp_get_num_threads();
    			printf("Number of threads = %d\n", nthreads);
   		}
  	}  /* All threads join master thread and disband */
}
