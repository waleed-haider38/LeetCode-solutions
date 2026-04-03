package main

func canConstruct(ransomNote string, magazine string) bool {

	var count [26]int

	for i := 0; i < len(magazine); i++ {
		count[magazine[i]-'a']++
	}

	for i := 0; i < len(ransomNote); i++ {
		if count[ransomNote[i]-'a'] == 0 {
			return false
		}
		count[ransomNote[i]-'a']--
	}

	return true
}