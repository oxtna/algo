def mergesort(list: list[int]) -> list[int]:
	if len(list) < 2:
		return list
	sorted_array = []
	left = mergesort(list[:len(list) // 2])
	right = mergesort(list[len(list) // 2:])
	while left and right:
		num_left = left[0]
		num_right = right[0]
		if num_left < num_right:
			sorted_array.append(num_left)
			left.remove(num_left)
		else:
			sorted_array.append(num_right)
			right.remove(num_right)
	if left:
		sorted_array.extend(left)
	else:
		sorted_array.extend(right)
	return sorted_array

if __name__ == "__main__":
	test_lists = [
		[1, 2, 3, 4],
		[-1, 4, -4, 0],
		[15, 2, 0, -3]
	]
	sorted_lists = [sorted(test_list) for test_list in test_lists]
	for test_list, sorted_list in zip(test_lists, sorted_lists):
		assert mergesort(test_list) == sorted_list
