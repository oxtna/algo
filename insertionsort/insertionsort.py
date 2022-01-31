def insertionsort(list: list[int]) -> None:
	for i in range(1, len(list)):
		for j in range(i):
			if list[i] < list[j]:
				tmp = list[j]
				list[j] = list[i]
				while j < i:
					j += 1
					list[j], tmp = tmp, list[j]


if __name__ == "__main__":
	test_lists = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_lists = [sorted(test_list) for test_list in test_lists]
	for test_list, sorted_list in zip(test_lists, sorted_lists):
		insertionsort(test_list)
		assert test_list == sorted_list
