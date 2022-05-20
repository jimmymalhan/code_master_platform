// two number sum

package main
import "fmt"

func twoNumberSum(array []int, target int) []int {
	for i := 0; i < len(array); i++ { 
		for j := i + 1; j < len(array); j++ {
			if array[i]+array[j] == target {
				return []int{array[i], array[j]}
			}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(twoNumberSum([]int{1, 2, 3, 4, 5}, 5))
}

// go run Arrays/two_number_sum.go