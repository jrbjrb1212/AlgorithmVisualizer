from Untill import *

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
                yield True
            elif lst[min_idx] != max_val and ascending:
                lst[j], lst[max_idx] = lst[max_idx], lst[j]
                draw_list(draw_info, {max_idx: draw_info.GREEN, j: draw_info.RED}, True)
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

        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending
            descending_sort = i > 0 and lst[i-1] > current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i-1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True
    
    return lst

def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]


            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                # quick way to swap with using temp variable
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)

                # avoids only running this method at a time
                yield True
    return lst


def merge_sort(draw_info, ascending = True):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
        for index in arr:
            print(index)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1