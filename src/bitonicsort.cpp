#include <stdint.h>
#include <stdlib.h>
#include <omp.h>
#include <iostream>

#define UP 0
#define DOWN 1

// must be a power of two
constexpr size_t SIZE = 1 << 24;
constexpr size_t MAX_VALUE = -1;
constexpr size_t THREADS = 8;
using T = uint64_t;

/// src:
/// https://www.cs.rutgers.edu/~venugopa/parallel_summer2012/bitonic_openmp.html
/// needs to be benchmarked against std::sort()
///
/// \param start 	start position in `seq` to start from
/// \param length 	number of elements to sort
/// \param seq 		array to sort
/// \param flag 	sorting direction.
/// 					1 = incrementing
/// 					else decrementing
/// \param m 		number of subparts
template<typename T> 
void bitonic_sort_par(const size_t start, const size_t length, T *seq, 
					  const int flag, const uint32_t m) {
  size_t i;
  size_t split_length;

  if (length == 1)
    return;

  if (length % 2 != 0) {
	std::cout << "The length of a (sub)sequence is not divided by 2.\n";
	exit(0);
  }

  split_length = length / 2;

  // bitonic split
	#pragma omp parallel for default(none) shared(seq, flag, start, split_length) private(i)
  for (i = start; i < start + split_length; i++) {
    if (flag == 1) {
      if (seq[i] > seq[i + split_length]) {
        std::swap(seq[i], seq[i + split_length]);
	  }	
    } else {
      if (seq[i] < seq[i + split_length]) {
        std::swap(seq[i], seq[i + split_length]);
	  }	
    }
  }

  if (split_length > m) {
  // m is the size of sub part-> n/numThreads
    bitonic_sort_par<T>(start, split_length, seq, flag, m);
    bitonic_sort_par<T>(start + split_length, split_length, seq, flag, m);
  }
}


template<typename T> 
void bitonic_sort_seq(const size_t start, const size_t length, T *seq, 
		              const int flag) {
    if (length == 1)
        return;

    if (length % 2 !=0 ) {
        printf("error\n");
        exit(0);
    }

    const size_t split_length = length / 2;

    // bitonic split
    for (size_t i = start; i < start + split_length; i++) {
        if (flag == UP) {
            if (seq[i] > seq[i + split_length])
                std::swap(seq[i], seq[i + split_length]);
        }
        else {
            if (seq[i] < seq[i + split_length])
                std::swap(seq[i], seq[i + split_length]);
        }
    }

    bitonic_sort_seq(start, split_length, seq, flag);
    bitonic_sort_seq(start + split_length, split_length, seq, flag);
}

template<typename T> 
void bitonic_sort(const size_t start, const size_t length, T *seq, 
				  const uint32_t threads) {

   	// the size of sub part
    const uint32_t m = length / threads;
	int flag;

    // make the sequence bitonic - part 1
    for (size_t i = 2; i <= m; i = 2 * i) {
		#pragma omp parallel for shared(i, seq) private(j, flag)
        for (size_t j = 0; j < length; j += i) {
            if ((j / i) % 2 == 0)
                flag = UP;
            else
                flag = DOWN;

            bitonic_sort_seq<T>(j, i, seq, flag);
        }
    }

    // make the sequence bitonic - part 2
    for (size_t i = 2; i <= threads; i = 2 * i) {
        for (size_t j = 0; j < threads; j += i) {
            if ((j / i) % 2 == 0)
                flag = UP;
            else
                flag = DOWN;

            bitonic_sort_par<T>(j*m, i*m, seq, flag, m);
        }
		
		#pragma omp parallel for shared(j)
        for (size_t j = 0; j < threads; j++) {
            if (j < i)
                flag = UP;
            else
                flag = DOWN;

            bitonic_sort_seq<T>(j*m, m, seq, flag);
        }
    }

}

int main() {
	srand(1337);
	
	omp_set_dynamic(0);
	omp_set_num_threads(THREADS); 

	int ret = 0;
	T *data = (T *)malloc(sizeof(T) * SIZE);

	// fill with random data
	#pragma omp parallel for
	for (size_t i = 0; i < SIZE; i++) {
		data[i] =  (uint64_t(rand()) << 32) | rand();
		data[i] %= MAX_VALUE;
 	}
	
	// sort
	bitonic_sort<T>(0, SIZE, data, THREADS);

	// check for correctness
	//for (size_t i = 0; i < SIZE-1; i++) {
	//	if (data[i] > data[i + 1]) {
	//		std::cout << i << ": " << data[i] << ":" << data[i+1] << "\n";
	//		ret = 1;
	//		break;
	//	}
	//}

	free(data);
	return ret;
}
