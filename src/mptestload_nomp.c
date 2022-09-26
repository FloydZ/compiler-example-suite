#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10000

int main(int argc, char *argv[]) {
  uint64_t i, j, nthreads, tid;
  double a[N], b[N], c[N], d[N];
  // const clock_t start = clock();

  /* Some initializations */
  for (i = 0; i < N; i++) {
    a[i] = i * 2;
    b[i] = i + 3;
    c[i] = d[i] = 1;
  }

  {

    {
      {
        for (j = 0; j < N; j++) {
          for (i = 0; i < N; i++) {
            c[i] += a[i] + b[i] * d[j];
          }

          for (i = 0; i < N; i++) {
            d[i] -= c[i] + b[j] * a[i];
          }
          a[j] += c[j] / d[j];
          b[j] -= d[j] / c[j];
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

  // printf("%f\n", (double)(clock()-start));
  return sum;
}
