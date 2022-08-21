// simple c++ quicksosrt
#include <stdint.h>
#include <stdlib.h>

constexpr size_t SIZE = 1000;
using T = uint64_t;


template<typename T> 
void swap(T *a, T *b) {
    const T t = *a;
    *a = *b;
    *b = t;
}

template<typename T> 
uint64_t partition (T arr[], const uint64_t low, const uint64_t high) {
    T pivot = arr[high];
    uint64_t i = low - 1;

    for (uint64_t j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

template<typename T> 
void quickSort(T arr[], const uint64_t low, const uint64_t high) {
    if (low < high) {
        uint64_t i = partition(arr, low, high);
        quickSort(arr, low, i - 1);
        quickSort(arr, i + 1, high);
    }
}

int main() {
	T *arr = (T *)malloc(sizeof(T) * SIZE);
	quickSort(arr, 0, SIZE);
	int ret = 0;

	// check for correctness
	for (size_t i = 0; i < SIZE-1; i++) {
		if (arr[i] > arr[i+1]) {
			ret = 1;
			break;
		}
	}

	free(arr);
	return ret;
}
