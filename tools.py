import time
import os
import functools
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
def crop_video(file, out, time= [150, 160]):
    ffmpeg_extract_subclip(file, time[0], time[1], targetname= os.path.join("videos", "%s.mp4" % out))


#crop_video("videos/Most Dramatic Comebacks In Football 2019.mp4")
crop_video("videos/Most Dramatic Comebacks In Football 2019.mp4", "crop_football")


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'timeit: {func}: {time.time() - start_time}s')
        return result
    return wrapper


#print(check('[{([[[]]])(){}}]'))

# Intersection. Return the intersection
def intersection(lst1, lst2):
    '''removes duplicates'''
    # order is not guaranteed unless call sorted(...) to sort again
    return list(set(lst1) & set(lst2))

# Return the intersection of two sorted arrays.

def intersect(lst1, lst2):
    '''reserves duplicates'''
    ans = []
    p1s, p1, p2 = 0, 0, 0
    while p2 < len(lst2) and p1s < len(lst1):
        if lst1[p1] == lst2[p2]:
            ans.append(lst1[p1])
            p1, p2 = p1 + 1, p2 + 1
            p1s=p1
        else: #elif lst1[p1] < lst2[p2]:
            p1 += 1
            if p1 >= len(lst1):
                p1, p2 = 0, p2 + 1
                # else:
        #     p2 += 1
    return ans

#print(intersect([7, 1, 2, 4, 6, 10], [2, 4, 5, 7, 10, 3]))


#Two sum. Given an array and a number N, return True if there are numbers A, B in the array such that A + B = N. Otherwise, return False.

def two_sum(numbers, target):
#    index = {num: i for (i, num) in enumerate(numbers)}
    n = len(numbers)
    for i in range(n):
        a = numbers[i]
        b = target - a

        if b in numbers[i:]:
            #j = numbers.index(b)
            return [a, b]
    return False

print(two_sum([3, 1, 3, 7], 5))

#Remove duplicates. Remove duplicates in list. The list is not sorted and the order of elements from the original list should be preserved.
def remove_duplicates(lst):
    new_list = []
    mentioned_values = set()
    for elem in lst:
        if elem not in mentioned_values:
            new_list.append(elem)
            mentioned_values.add(elem)
    return new_list


# Flip a binary tree. Write a function for rotating a binary tree.
#   The definition of a tree node: Node(value, left, right)

def flip_bt(head):
    if head is not None:
        head.left, head.right = head.right, head.left
        flip_bt(head.left)
        flip_bt(head.right)


def sort_dictionary(dictionary):
    list_of_sorted_pairs = {k:dictionary[k] for k in sorted(dictionary.keys(), key=dictionary.get, reverse=False)}
    # Так мы создаём кортежи (ключ, значение) из отсортированных элементов по ключу равному "значение ключа"
    # Также отсортированы будут и ключи, имеющие одно значение
    # "reverse = False" говорит, что перебор нужно делать в обычном порядке
    # Если нужно отсортировать значения в обратном порядке, то reverse можно сделать = True
    return list_of_sorted_pairs

sort_dictionary({1:7, 7:3})