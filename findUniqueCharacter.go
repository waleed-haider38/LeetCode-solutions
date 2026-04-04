package main

func firstUniqChar(s string) int {

	var findUnique [26]int

	for i := 0; i < len(s); i++ {
		findUnique[s[i]-'a']++
	}

	for i := 0; i < len(s); i++ {
		if findUnique[s[i]-'a'] == 1 {
			return i
		}
	}

	return -1
}