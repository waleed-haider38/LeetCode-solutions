package main

func intersection(nums1 []int, nums2 []int) []int {

	set := make(map[int]bool)
	result := []int{}

	// Step 1: nums1 ke elements set mein daal do
	for _, num := range nums1 {
		set[num] = true
	}

	// Step 2: nums2 traverse karo
	for _, num := range nums2 {
		if set[num] {
			result = append(result, num)
			delete(set, num) // taake duplicate na aaye
		}
	}

	return result
}