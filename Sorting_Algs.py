from Untill import *
# imports modules
import pygame
import random
import math

pygame.init()

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    i = 0
    j = len(lst) - 1
    print(ascending)
    while i < j:
        min_idx = i
        max_idx = i
        max_val = lst[i]
        if ascending:
            for k in range(i, j+1):
                if lst[min_idx] > lst[k]:
                    min_idx = k
                if lst[max_idx] < lst[k] and ascending:
                    max_idx = k
                    max_val = lst[k]
                    draw_list(draw_info, {max_idx: draw_info.GREEN, k: draw_info.RED}, True)


            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            draw_list(draw_info, {min_idx: draw_info.GREEN, i: draw_info.RED}, True)


            # Edge-case: if we shifted the value to the maximum in the last swap
            if lst[min_idx] == max_val and ascending:
                lst[j], lst[min_idx] = lst[min_idx], lst[j]
                draw_list(draw_info, {min_idx: draw_info.GREEN, j: draw_info.RED}, True)
                # update list
                yield True
            elif lst[min_idx] != max_val and ascending:
                lst[j], lst[max_idx] = lst[max_idx], lst[j]
                draw_list(draw_info, {max_idx: draw_info.GREEN, j: draw_info.RED}, True)
                # update list
                yield True

            i += 1
            j -= 1

        else:
            for k in range(i, j+1):
                if lst[max_idx] < lst[k]:
                    max_idx = k
                    max_val = lst[k]
                    draw_list(draw_info, {max: draw_info.GREEN, k: draw_info.RED}, True)
                if lst[min_idx] > lst[k]:
                    min_idx = k
                    min_idx = lst[k]
                    draw_list(draw_info, {min_idx: draw_info.GREEN, k: draw_info.RED}, True)


            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            draw_list(draw_info, {min_idx: draw_info.GREEN, i: draw_info.RED}, True)
            # update list
            yield True


            # Edge-case: if we shifted the value to the maximum in the last swap
            if lst[min_idx] == max_val:
                lst[j], lst[min_idx] = lst[min_idx], lst[j]
                draw_list(draw_info, {min_idx: draw_info.GREEN, j: draw_info.RED}, True)
                yield True
            elif lst[min_idx] != max_val:
                lst[j], lst[max_idx] = lst[max_idx], lst[j]
                draw_list(draw_info, {max_idx: draw_info.GREEN, j: draw_info.RED}, True)
                
                yield True
            
            i += 1
            j -= 1

    return lst



def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        # default selection sort alg
        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending
            descending_sort = i > 0 and lst[i-1] > current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i = i - 1
            lst[i] = current
            # update list
            draw_list(draw_info, {i-1: draw_info.GREEN, i: draw_info.RED}, True)
            # yield true for easy acess
            yield True
    
    return lst

def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst

    # default bubble sort alg
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]


            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                # quick way to swap with using temp variable
                # update list
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)

                # avoids only running this method at a time
                yield True
    return lst

# driver method for merge sort 
def merge_intro(draw_info, ascending = True):
    lst = draw_info.lst
    merge_sort(draw_info, lst, 0, len(lst)-1, ascending) 
    while(True):
        yield True

# core split method for mergesort
def merge_sort(draw_info, arr, left, right, ascending):
    if left < right:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        mid = left+(right-left)//2
 
        # Sort first and second halves
        draw_list(draw_info, {left: draw_info.BLUE, mid: draw_info.BLUE}, True)
        merge_sort(draw_info, arr, left, mid,ascending)

        draw_list(draw_info, {mid+1: draw_info.BLUE, right: draw_info.BLUE}, True)
        merge_sort(draw_info, arr, mid+1, right, ascending)

        merge(draw_info, arr, left, mid, right, ascending)

# core merging method for mergesort
def merge(draw_info, arr, left, mid, right, ascending):
    n1 = mid - left + 1
    n2 = right - mid
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]
 
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray
 
    # 
    while i < n1 and j < n2:
        if ascending:
            if L[i] <= R[j]:
                draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN}, True)
                arr[k] = L[i]
                i += 1
            else:
                draw_list(draw_info, {k: draw_info.RED, j: draw_info.GREEN}, True)
                arr[k] = R[j]
                j += 1

        else:
            if L[i] >= R[j]:
                draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN}, True)
                arr[k] = L[i]
                i += 1
            else:
                draw_list(draw_info, {k: draw_info.RED, j: draw_info.GREEN}, True)
                arr[k] = R[j]
                j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        draw_list(draw_info, {k: draw_info.RED, i: draw_info.GREEN}, True)
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        draw_list(draw_info, {k: draw_info.RED, j: draw_info.GREEN}, True)
        arr[k] = R[j]
        j += 1
        k += 1


def quick_sort_intro(draw_info, ascending=True):
    lst = draw_info.lst
    quickSort(draw_info, lst, 0, len(lst) -1, ascending)
    while(True):
        yield True


def partition(draw_info, arr, low, high, ascending):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if ascending:
            if arr[j] <= pivot:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
        else:
            if arr[j] >= pivot:
                i=i+1
                arr[i], arr[j] = arr[j], arr[i]
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)

 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
def quickSort(draw_info, arr, low, high, ascending):
    if len(arr) == 1:
        return arr
    
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(draw_info, arr, low, high, ascending)
 
        # Separately sort elements before
        # partition and after partition
        draw_list(draw_info, {low: draw_info.BLUE, pi-1: draw_info.BLUE}, True)
        quickSort(draw_info, arr, low, pi-1, ascending)

        draw_list(draw_info, {pi+1: draw_info.BLUE, high: draw_info.BLUE}, True)
        quickSort(draw_info, arr, pi+1, high, ascending)
        