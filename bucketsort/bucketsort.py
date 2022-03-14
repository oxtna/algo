def bucketsort(array: list[int]) -> None:
	if min(array) == max(array):
		return array
	buckets = [[] for _ in range(len(array))]
	for x in array:
		bucket_index = int(len(array) * (x - min(array)) / (max(array) - min(array)))
		if bucket_index == len(array):
			bucket_index -= 1
		buckets[bucket_index].append(x)

	def insertion_sort(array: list[int]) -> None:
			for i in range(1, len(array)):
				for j in range(i):
					if array[i] < array[j]:
						tmp = array[j]
						array[j] = array[i]
						while j < i:
							j += 1
							array[j], tmp = tmp, array[j]

	for bucket in buckets:
		insertion_sort(bucket)
	index = 0
	for bucket in buckets:
		for x in bucket:
			array[index] = x
			index += 1

if __name__ == "__main__":
	test_arrays = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_arrays = [sorted(test_array) for test_array in test_arrays]
	for test_array, sorted_array in zip(test_arrays, sorted_arrays):
		bucketsort(test_array)
		assert test_array == sorted_array
