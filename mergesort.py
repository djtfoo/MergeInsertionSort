import time

class MergeSort:
    key_comp = 0
    
    # For running the algorithm to sort an array and print the result
    def run(self, arr):
        self.key_comp = 0
        start = time.perf_counter()
        sorted_arr = arr.copy()
        self.merge_sort_kc(sorted_arr, 0, len(sorted_arr) - 1)
        end = time.perf_counter()

        print("\nYour sorted array is: " + str(sorted_arr))
        print("It took you " + str((end-start)*100) + " * 10^-2 seconds to complete the sort")
        print("No. Key Comparisons: " + str(self.key_comp))
    
    # Get the run time of the algorithm to sort the given array
    def run_time(self, arr):
        sorted_arr = arr.copy()
        
        start = time.perf_counter()
        self.merge_sort(sorted_arr, 0, len(sorted_arr) - 1)
        end = time.perf_counter()
        
        del sorted_arr
        return end-start
    
    # Get the number of key comparisons made by the algorithm to sort the given array
    def run_keycomp(self, arr):
        self.key_comp = 0
        sorted_arr = arr.copy()
        
        self.merge_sort_kc(sorted_arr, 0, len(sorted_arr) - 1)

        del sorted_arr
        return self.key_comp
    
###########################################################################
#### Merge Sort
    
    # Merge Sort algorithm
    def merge_sort(self, arr, first, last):        
        # Base case
        if last - first <= 0:
            return
        
        mid = (int)((first+last)/2)
        if last - first > 1:    # 2 elements or more
            self.merge_sort(arr, first, mid)    # sort first half
            self.merge_sort(arr, mid+1, last)   # sort second half
        self.merge(arr, first, mid, last)   # merge two halves

    # Merge function
    def merge(self, arr, first, mid, last):
        a = first
        b = mid + 1
        while a <= mid and b <= last:
            if arr[a] < arr[b]:
                a += 1
            elif arr[b] < arr[a]:
                temp = arr[b]
                arr.pop(b)
                arr.insert(a, temp)    # insert at where a is
                a += 1
                mid += 1
                b += 1
            else:
                temp = arr[b]
                arr.pop(b)
                arr.insert(a, temp)    # insert at where a is
                a += 2
                mid += 1
                b += 1
                
###########################################################################
#### Merge Sort w/ Key Comparions Count
                
    # Merge Sort algorithm with key comparisons count
    def merge_sort_kc(self, arr, first, last):        
        # Base case
        if last - first <= 0:
            return
        
        mid = (int)((first+last)/2)
        if last - first > 1:    # 2 elements or more
            self.merge_sort_kc(arr, first, mid)    # sort first half
            self.merge_sort_kc(arr, mid+1, last)   # sort second half
        self.merge_kc(arr, first, mid, last)   # merge two halves

    # Merge function with key comparisons count
    def merge_kc(self, arr, first, mid, last):
        a = first
        b = mid + 1
        while a <= mid and b <= last:
            self.key_comp += 1    # 1 key comparison
            if arr[a] < arr[b]:
                a += 1
            elif arr[b] < arr[a]:
                temp = arr[b]
                arr.pop(b)
                arr.insert(a, temp)    # insert at where a is
                a += 1
                mid += 1
                b += 1
            else:
                temp = arr[b]
                arr.pop(b)
                arr.insert(a, temp)    # insert at where a is
                a += 2
                mid += 1
                b += 1


class ModifiedMergeSort(MergeSort):
    
    def __init__(self, S):
        self.S_val = S
        
    def set_S(self, S):
        self.S_val = S
        
###########################################################################
#### Merge Sort
        
    # Override Merge Sort algorithm
    def merge_sort(self, arr, first, last):        
        # Base case
        if last - first <= 0:
            return
        
        # If the size of the array is less than or equal to S, carry out insertion sort
        if last - first < self.S_val:
            self.insertion_sort(arr, first, last)
        else:
            mid = (int)((first+last)/2)
            self.merge_sort(arr, first, mid)    # sort first half
            self.merge_sort(arr, mid+1, last)   # sort second half
            self.merge(arr, first, mid, last)   # merge two halves
        
    # Switch to insertion sort when array size is below S
    def insertion_sort(self, arr, first, last):
        for i in range(first+1, last+1):
            for j in range(i, first, -1):
                if arr[j] < arr[j-1]:
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                else:
                    break
                    
###########################################################################
#### Merge Sort w/ Key Comparions Count
                    
    # Override Merge Sort algorithm with key comparisons
    def merge_sort_kc(self, arr, first, last):        
        # Base case
        if last - first <= 0:
            return
        
        # If the size of the array is less than or equal to S, carry out insertion sort
        if last - first < self.S_val:
            self.insertion_sort_kc(arr, first, last)
        else:
            mid = (int)((first+last)/2)
            self.merge_sort_kc(arr, first, mid)    # sort first half
            self.merge_sort_kc(arr, mid+1, last)   # sort second half
            self.merge_kc(arr, first, mid, last)   # merge two halves
        
    # Insertion sort when array size is below S, with key comparisons count
    def insertion_sort_kc(self, arr, first, last):
        for i in range(first+1, last+1):
            for j in range(i, first, -1):
                self.key_comp += 1    # 1 key comparison
                if arr[j] < arr[j-1]:
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                else:
                    break