#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

comp = 0

#file to list of numbers
def parse(txt):
    f = open(txt, "r")
    buffer = f.read()
    buffer =  buffer.replace("\n", " ")
    buffer =  buffer.replace("\t", " ")
    numbers = buffer.split(" ")
    result = list(map(float, numbers))
    return result

def bubble_sort(nb_lst):
    for j in range(len(nb_lst), 0, -1):
        for i in range(0, j - 1):
            globals()['comp'] += 1
            if nb_lst[i] > nb_lst[i + 1]:
                nb_temp = nb_lst[i + 1]
                nb_lst[i + 1] = nb_lst[i]
                nb_lst[i] = nb_temp
    #print("Bubble result:", nb_lst)
    return nb_lst

def select(nb_lst):
    offset = 0
    while offset + 1 != len(nb_lst):
        smallest = nb_lst[offset]
        smallest_i = offset
        for i in range(offset + 1, len(nb_lst)):
            globals()['comp'] += 1
            if nb_lst[i] < smallest:
                smallest = nb_lst[i]
                smallest_i = i
        temp = nb_lst[offset]
        nb_lst[offset] = smallest
        nb_lst[smallest_i] = temp
        offset += 1
    return nb_lst

#Pas encore bon / copié
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        globals()['comp'] += 1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            if key < arr[j]:
                globals()['comp'] += 1
        arr[j+1] = key 

def quick_part(nb_lst, first, last, pivot):
    nb_lst[pivot], nb_lst[last] = nb_lst[last], nb_lst[pivot]
    j = first
    for i in range(first, last):
        globals()['comp'] += 1
        if nb_lst[i] <= nb_lst[last]:
            nb_lst[i], nb_lst[j] = nb_lst[j], nb_lst[i]
            j += 1
    nb_lst[last], nb_lst[j] = nb_lst[j], nb_lst[last]
    return j

#Pas encore bon
def quick_sort(nb_lst, first, last):
    if first < last:
        pivot = first
        pivot = quick_part(nb_lst, first, last, pivot)
        quick_sort(nb_lst, first, pivot-1)
        quick_sort(nb_lst, pivot + 1, last)
    return nb_lst

if len(sys.argv) != 2:
    exit(84)
numbers = parse(sys.argv[1])
comp = 0
selectres = select(numbers.copy())
print("Selection sort:", comp, "comparisons")
comp = 0
bubble = bubble_sort(numbers.copy())
print("Bubble sort:", comp, "comparisons")
comp = 0
insertionres = insertion(numbers.copy())
print("Insertion sort:", comp, "comparisons")
comp = 0
quick = quick_sort(numbers.copy(), 0, len(numbers) - 1)
print(quick)
print("Quicksort:", comp, "comparisons")
exit(0)