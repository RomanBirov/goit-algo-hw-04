import random
import timeit


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def measure_time(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=1)


def generate_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]


def main():
    sizes = [1000, 5000, 10000]

    print("\n=== Sorting Performance Comparison ===\n")

    results = {}

    for size in sizes:
        print(f"Dataset size: {size}")

        data = generate_data(size)
        results[size] = {}

        if size <= 5000:
            t_ins = measure_time(insertion_sort, data)
            results[size]["insertion"] = t_ins
            print(f"  Insertion Sort:   {t_ins:.5f} sec")
        else:
            results[size]["insertion"] = None
            print("  Insertion Sort:   skipped (too slow)")

        t_merge = measure_time(merge_sort, data)
        results[size]["merge"] = t_merge
        print(f"  Merge Sort:       {t_merge:.5f} sec")

        t_timsort = measure_time(sorted, data)
        results[size]["timsort"] = t_timsort
        print(f"  Timsort:          {t_timsort:.5f} sec\n")

    print("\n=== Summary Result Table (seconds) ===")
    for size, res in results.items():
        print(f"\nArray size: {size}")
        print(f"  Insertion Sort: {res['insertion']}")
        print(f"  Merge Sort:     {res['merge']}")
        print(f"  Timsort:        {res['timsort']}")


if __name__ == "__main__":
    main()