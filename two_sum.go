package main

import (
	"fmt"
)

func main(){
	nums := []int{2 , 7, 11 , 14}

	m := make(map[int]int)

	for _ , num := range nums {
		m[num]++
	}
	fmt.Println(m)

	

}