package main


func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    var sourceAlphabetCounter [26]int
    var targetAlphabetCounter [26]int

    for i:= 0; i < len(s); i++ {
        sourceAlphabetCounter[s[i] - 'a']++
        targetAlphabetCounter[t[i] - 'a']++
    }

    for j:= 0; j < 26 ; j++ {
        if sourceAlphabetCounter[j] != targetAlphabetCounter[j] {
            return false
        } 
    }
    return true
}