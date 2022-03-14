package main

import "fmt"

func main() {
	
	// even odd
	i := 1
	for i <= 3 {
		// flow control
		if i % 2 == 0 {
			fmt.Println( i , "Value is even")
		} else if i % 2 == 1 {
			fmt.Println( i , "Value is odd")
		} else {
			fmt.Println( i , "This isn't a number")
		}
		i++
	}

	j := 3
	// switch
	switch j {
	case 1:
		fmt.Println("i is 1")
	case 2:
		fmt.Println("i is 2")
	case 3:
		fmt.Println("i is 3")
	}

	k := 0
	// arrays
	var a [5]int
	fmt.Println("empty array:", a)

	for k <= 4 {
		a[k] = k
		k++
	}
	// a[4] = 10
	fmt.Println(a)

	// slices
	s := make([]string, 3)
	fmt.Println("empty slice", s)

	s[0] = "a"
	s[1] = "b"
	s[2] = "yomama"

	fmt.Println(s)

	s = append(s, "d", "e", "f")
	fmt.Println(s)

	p := s[2:5]
	fmt.Println(p)
}