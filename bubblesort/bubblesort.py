def bubblesort(list: list[int]) -> None:
	sorted = False
	while not sorted:
		sorted = True
		for i in range(len(list) - 1):
			if list[i] > list[i + 1]:
				sorted = False
				list[i], list[i + 1] = list[i + 1], list[i]


if __name__ == "__main__":
	test_lists = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_lists = [sorted(test_list) for test_list in test_lists]
	for test_list, sorted_list in zip(test_lists, sorted_lists):
		bubblesort(test_list)
		assert test_list == sorted_list
