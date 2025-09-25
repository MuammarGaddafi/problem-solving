#include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int* start = arr;
    int temp;
    int length = (sizeof(arr) / sizeof(arr[0]));
    int* end = arr + length - 1;

    int i = 0;
    while (i < (length / 2)) {
        int temp = *start;
        *start = *end;
        *end = temp;

        i += 1;
        start += 1;
        end -= 1;
    }

    for (i = 0; i < length; i++) {
        std::cout << arr[i] << " ";
    }

    return 0;
}
