package main

import "sort"

func maxFrequencyElements(nums []int) int {
    sort.Ints(nums)

    currentFreq := 1
    maxFreq := 0
    totalCount := 0

    for i:= 0; i<len(nums)-1 ; i++ {
        if nums[i]== nums[i+1]{
            currentFreq++
        }else{
            if currentFreq > maxFreq {
                maxFreq =  currentFreq
                totalCount = currentFreq
            }else if currentFreq ==  maxFreq {
                totalCount += currentFreq
            }
            currentFreq = 1
        }

    }
    if currentFreq > maxFreq {
        maxFreq = currentFreq
        totalCount = currentFreq
    }else if currentFreq ==  maxFreq {
        totalCount += currentFreq

    }
    return totalCount

    
}