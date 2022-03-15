def heapsort(array: list[int]) -> None:
	def heapify(array: list[int], index: int) -> None:
		left_index = 2 * index + 1
		right_index = left_index + 1
		if len(array) > right_index:
			if array[left_index] > max(array[right_index], array[index]):
				array[left_index], array[index] = array[index], array[left_index]
				heapify(array, left_index)
			elif array[right_index] > max(array[left_index], array[index]):
				array[right_index], array[index] = array[index], array[right_index]
				heapify(array, right_index)
		elif len(array) > left_index:
			if array[left_index] > array[index]:
				array[left_index], array[index] = array[index], array[left_index]
				heapify(array, left_index)

	def pop_max_and_insert(heap: list[int], index_of_last: int) -> None:
		heap[0], heap[index_of_last] = heap[index_of_last], heap[0]
		current_index = 0
		left_index = 2 * current_index + 1
		right_index = left_index + 1
		while left_index < index_of_last:
			if right_index < index_of_last:
				if heap[current_index] > max(heap[left_index], heap[right_index]):
					break
				if heap[left_index] > heap[right_index]:
					heap[current_index], heap[left_index] = heap[left_index], heap[current_index]
					current_index = left_index
				else:
					heap[current_index], heap[right_index] = heap[right_index], heap[current_index]
					current_index = right_index
			else:
				if heap[current_index] > heap[left_index]:
					break
				if heap[left_index] > heap[current_index]:
					heap[current_index], heap[left_index] = heap[left_index], heap[current_index]
					current_index = left_index
			left_index = 2 * current_index + 1
			right_index = left_index + 1

	for index in range(len(array) - 1, -1, -1):
		heapify(array, index)
	for index in range(len(array) - 1, 0, -1):
		pop_max_and_insert(array, index)


if __name__ == "__main__":
	test_arrays = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_arrays = [sorted(test_array) for test_array in test_arrays]
	for test_array, sorted_array in zip(test_arrays, sorted_arrays):
		heapsort(test_array)
		assert test_array == sorted_array
