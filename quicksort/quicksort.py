def quicksort(array: list[int], first: int = None, last: int = None) -> None:
	def partition(array: list[int], first: int, last: int) -> int:
		pivot = (first + last) // 2
		while first < last:
			while array[pivot] > array[first]:
				first += 1
			while array[pivot] < array[last]:
				last -= 1
			if first < last:
				array[first], array[last] = array[last], array[first]
		array[pivot], array[last] = array[last], array[pivot]
		return last
		
	if first is None:
		first = 0
	if last is None:
		last = len(array) - 1
	if first < last:
		pivot = partition(array, first, last)
		quicksort(array, first, pivot)
		quicksort(array, pivot + 1, last)

if __name__ == "__main__":
	test_lists = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_lists = [sorted(test_list) for test_list in test_lists]
	for test_list, sorted_list in zip(test_lists, sorted_lists):
		quicksort(test_list)
		assert test_list == sorted_list
