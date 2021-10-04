#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import copy
import os

class comp:
    def __init__(self):
        self.staticvariable = 0
    def reset(self):
        self.staticvariable = 0
    def increment(self):
        self.staticvariable += 1
    def getComp(self):
        return(self.staticvariable)

def usage():
    print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\tfile that contains the numbers to be sorted, separated by space")
    exit(0)

def parse(txt):
    if not os.path.isfile(txt):
        exit(84)
    f = open(txt, "r")
    buffer = f.read()
    buffer =  buffer.replace("\n", " ")
    buffer =  buffer.replace("\t", " ")
    numbers = buffer.split(" ")
    for i in range(len(numbers)):
        if numbers[i] == '':
            del numbers[i]
    for i in numbers:
        for j in i:
            if j not in "0123456789- .":
                exit(84)
    result = list(map(float, numbers))
    return result

def bubble_sort(nb_lst, comparisons):
    for j in range(len(nb_lst), 0, -1):
        for i in range(0, j - 1):
            comparisons.increment()
            if nb_lst[i] > nb_lst[i + 1]:
                nb_temp = nb_lst[i + 1]
                nb_lst[i + 1] = nb_lst[i]
                nb_lst[i] = nb_temp
    return nb_lst

def select(nb_lst, comparisons):
    offset = 0
    while offset + 1 != len(nb_lst):
        smallest = nb_lst[offset]
        smallest_i = offset
        for i in range(offset + 1, len(nb_lst)):
            comparisons.increment()
            if nb_lst[i] < smallest:
                smallest = nb_lst[i]
                smallest_i = i
        temp = nb_lst[offset]
        nb_lst[offset] = smallest
        nb_lst[smallest_i] = temp
        offset += 1
    return nb_lst

def insertion(nb_lst, comparisons):
    for i in range(1, len(nb_lst)):
        nb_lst.insert(0, nb_lst[i])
        nb_lst.pop(i + 1)
        j = 0
        if j < i:
            comparisons.increment()
        while j < i and nb_lst[j + 1] <= nb_lst[j]:
            nb_lst[j], nb_lst[j + 1] = nb_lst[j + 1], nb_lst[j]
            j = j + 1
            if j < i:
                comparisons.increment()
    return(nb_lst)

def partition(nb_lst, pivot, comparisons):
    first = []
    second = []
    for i in range(1, len(nb_lst)):
        comparisons.increment()
        if nb_lst[i] < pivot:
            first.append(nb_lst[i])
        else:
            second.append(nb_lst[i])
    return first, second

def quick_sort(nb_lst, comparisons):
    if len(nb_lst) > 1:
        part = partition(nb_lst, nb_lst[0], comparisons)
        rl = quick_sort(part[0], comparisons)
        rr = quick_sort(part[1], comparisons)
        nb_lst = rl + [nb_lst[0]] + rr
    return nb_lst

def merging(left, right, comparisons):
    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        comparisons.increment()
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1
    return temp

def mergeSort(nb_lst, comparisons):
    if len(nb_lst) > 1:
        mid = int(len(nb_lst) / 2)
        start = mergeSort(nb_lst[:mid], comparisons)
        end = mergeSort(nb_lst[mid:], comparisons)
        return merging(start, end, comparisons)
    return nb_lst

def main(ac, av):
    if ac != 2:
        exit(84)
    if av[1] == "-h":
        usage()
    numbers = parse(av[1])
    if len(numbers) <= 1:
        return
    comparisons = comp()
    #select sort
    select(copy.deepcopy(numbers), comparisons)
    print('Selection sort:', comparisons.getComp(), "comparisons")
    #insertion sort
    comparisons.reset()
    insertion(copy.deepcopy(numbers), comparisons)
    print("Insertion sort:", comparisons.getComp(), "comparisons")
    #bubble sort
    comparisons.reset()
    bubble_sort(copy.deepcopy(numbers), comparisons)
    print ("Bubble sort:", comparisons.getComp(), "comparisons")
    #quicksort
    comparisons.reset()
    quick_sort(copy.deepcopy(numbers), comparisons)
    print("Quicksort:", comparisons.getComp(), "comparisons")
    #merge sort
    comparisons.reset()
    mergeSort(copy.deepcopy(numbers), comparisons)
    print("Merge sort:", comparisons.getComp(), "comparisons")

if __name__ == "__main__":
    main(len(sys.argv) ,sys.argv)
    exit(0)