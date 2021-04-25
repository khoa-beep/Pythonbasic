from collections import Counter
import math
from typing import Mapping


def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    sum_ = 0
    seen = set()
    for c in s1:
        if(c in c2 and c not in seen):
            sum_ += c2[c] if c1[c] > c2[c] else c1[c]
            seen.add(c)
    return sum_


def evenDigitsNumber(arr):
    res = 0
    for num in arr:
        if(len(str(num)) % 2 == 0):
            res = res + 1
    return res


def primeSquare(a, b):
    num = (a - b) * (a + b)
    if num < 2:
        return False
    if ((num == 2) or num == 3):
        return True
    max = int(math.sqrt(num)) + 1
    for i in range(3, max, 2):
        if(num % i == 0):
            return False
    return True


def maxComNumbers(n):
    if(n % 4 == 0):
        return n // 4
    elif (n % 4 == 1 and n >= 9):
        return 1 + (n-9)/4
    elif (n % 4 == 2 and n >= 6):
        return 1 + (n-6)/4
    elif (n % 4 == 3 and n >= 15):
        return 2 + (n-6-9)/4
    else:
        return -1
# Ý tưởng là đưa về 4 nhiều nhất có thể
# Case 1 : n % 4 == 0 => return n / 4;
# Case 2 : n % 4 == 1 => đưa về số % 4 = 1 nhỏ nhất và còn lại chia 4 => return 1 + (n - 9) / 4 , điều kiện của Case này là n >= 9
# Case 3 : n % 4 == 2 => ý tưởng như Case 2 , return 1 + (n - 6) / 4 , điều kiện của Case này là n >= 6
# Case 4 : n % 4 == 3 => ý tưởng như Case 2 , return 2 + (n - 6 - 9 ) / 4 , điều kiện case này là n >= 15
# Default : return -1;


def sum_of_cubes_odd_number(n):
    if (n <= 0):
        return -1
    else:
        sum = 0
        for i in range(1, n+1):
            sum += pow(2*i-1, 3)
        return sum % (10**9+7)


def plantFlowers(arr, n):
    arr = [0]+arr+[0]
    i = 0
    z = 0
    for x in range(len(arr)-1):
        if arr[x] == arr[x+1] == 0:
            i += 1
        else:
            i = 0
        if i == 2:
            z += 1
            i = 0
    return n <= z


def min_max(n):
    n = sorted(str(n))
    k = n[::-1]
    return int("".join(k)) - int("".join(n))


def minSwaps(arr):
    c = 0
    l = 0
    for i in range(len(arr)):
        if (i % 2 == 0):
            if(arr[i] % 2 != 0):
                c = c + 1
        else:
            if (arr[i] % 2 == 0):
                l = l + 1
    return -1 if c !=l else c

