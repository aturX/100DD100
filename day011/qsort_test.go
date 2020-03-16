package main

import "testing"

func TestQuickSort(t *testing.T) {
	values := []int{1,5,3,7,2}

	QuickSort(values)
	if values[0] != 1 || values[1] != 5 || values[2] != 3 || values[3] != 7 || values[4] != 2{
		t.Error("QuickSort() failed . Got: ",values,"Excepted: {1,2,3,5,7}")
	}

}

func TestQuickSort3(t *testing.T) {
	values := []int{5}
	QuickSort(values)
	if values[0] != 5{
		t.Error("BubbleSort() failed. Got ", values, "Excepted {5}")
	}
}