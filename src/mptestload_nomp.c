#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 1000

int main(int argc, char *argv[]) {
  uint64_t i, j, nthreads, tid;
  uint64_t *a = (uint64_t *)malloc(8 * N),
		   *b = (uint64_t *)malloc(8 * N), 
		   *c = (uint64_t *)malloc(8 * N),
		   *d = (uint64_t *)malloc(8 * N);
  const clock_t start = clock();

  /* Some initializations */
  for (i = 0; i < N; i++) {
    a[i] = i * 2 + b[i];
    b[i] = i + 3 - a[i];
    c[i] = d[i] = 1;
  }
	
  for (uint64_t k = 0; k < N; k++){
    {
      {
        for (j = 0; j < N; j++) {
          for (i = 0; i < N; i++) {
            c[i] += a[i] + b[i] * d[j];
          }

          for (i = 0; i < N; i++) {
            d[i] -= c[i] + b[j] * a[i];
          }
          a[j] += c[j] * d[j];
          b[j] -= d[j] * c[j];
        }
      }

      {
        for (i = 0; i < N; i++) {
          d[i] -= a[i] * b[i] + c[i];
        }
      }
    }

  }

  int sum = 0;
  for (uint64_t i = 0; i < N; i++) {
    sum += d[i] - c[i];
  }

  printf("%f\n", (double)(clock()-start));
  free(a);
  free(b);
  free(c);
  free(d);
  return !(sum > 0);
}
