# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#BÀI 1 
def question_1(n: int) -> bool:
    if n < 2:
        return False 
    for i in range(2,n):
        if n%i == 0:
            print("khong phai la so nguyen")
            return False
    print("la so nguyen")
    return True
print(question_1(11))
print(question_1(4))

#bài 2
import random
def question_2(n: int) -> (int, float):
   tong = 0
   for i in range(n):
       so = random.randint(1,100)
       print("Số ngẫu nhiên: ",so)
       tong += so 
   tb = tong / n
   return tong, tb  

if __name__=="__main__":
    print(question_2(5))
    print(question_2(10))
    
#bài 3
def question_3(s: str) -> (int, int):
    hoa = 0
    thuong = 0
    for i in s:
        if i.isupper():
            hoa += 1
        elif i.islower():
            thuong += 1
    return (hoa, thuong)

if __name__=="__main__":
    print(question_3("Hello World"))
    print(question_3("Python Programming"))
    
#Bài 4
def question_4(n: int) -> bool:
    if n % 2 == 0:
        print("so chẵn")
        return True
    elif n % 2 != 0:
        print("so lẽ")
        return False
    
if __name__=="__main__":
    print(question_4(4))
    print(question_4(7))
    
#bài 5
def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    return None

if __name__=="__main__":    
    print(question_5([1, 2, 3, 4, 5], 3))
    print(question_5([10, 20, 30, 40], 25))

#bài 6
def question_6(n: int) -> int:
    ket_qua = 1
    for i in range(1, n+1):
        ket_qua *= i
    return ket_qua

if __name__=="__main__":
    print(question_6(5))
    print(question_6(7))
    
#bài 7
import random 
def question_7(n: int) -> (float, float):
    lon = 0
    nho = 1
    for i in range(n):        
        so = random.uniform(0,1)
        print("Số ngẫu nhiên: ",so)
        lon = max(lon,so)
        nho = min(nho,so)
    return lon,nho
    
if __name__=="__main__":
    print(question_7(5))
    print(question_7(10))

#bài 8
def question_8(s: str) -> str:
    return s[:: -1]
a= input("Nhập chuỗi: ")
print(question_8(a))
 
#bài 9
def question_9(s: str) -> bool:
    s = s.lower()
    chuoi = [i for i in s if i.isalnum()]
    return chuoi == chuoi[::-1]
 
if __name__ == "__main__":
     print(question_9("race a car"))
     print(question_9("A man, a plan, a canal: Panama"))

#bài 10
def question_10() -> None:
    ds = input("Nhập vào danh sách số nguyên: ")
    if not ds:
        return None
    ds_so_nguyen = [int(i) for i in ds.split()]
    return ds_so_nguyen

if __name__=="__main__":
    print(question_10())

# bài 11
def question_11(n: int) -> int:
    F0 = 0
    F1 = 1
    for i in range(n - 1):
        Fn = F0 + F1
        F0, F1 = F1, Fn
    return Fn

if __name__ == "__main__":
    print(question_11(5))
    print(question_11(10))
    
#bài 12
import random
def question_12() -> bool:
    n = random.randint(1, 1000)
    print(f"Số ngẫu nhiên: {n}")
    if n <= 1:
        print("không phải là số nguyên tố")
        return False
    for i in range(2, n):
        if n % i == 0:
            print("không phải là số nguyên tố")
            return False
    print("là số nguyên tố")
    return True

if __name__ == "__main__":
    print(question_12())
    
#bài 13
def question_13(s: str) -> int:
    cac_tu = s.split()
    return len(cac_tu)

if __name__ == "__main__":
     print(question_13("Hello word"))
     
#bài 14
def question_14(s: str) -> bool:
    return s.isdigit()

if __name__ == "__main__":
     print(question_14("123"))
     print(question_14("123a45"))

#bài 15
def question_15(value) -> bool:
    return value is None

if __name__=="__main__":
    print(question_15(None))
    print(question_15("13"))

#bài 16
def question_16(*agrs) -> float:
    if not agrs:
        return None
    trung_binh = sum(agrs) / len(agrs)
    return trung_binh
if __name__ == "__main__":
    print(question_16(10,20))
    print(question_16(1,2,3,4,5))

#bài 17
import random
def question_17(n: int) -> list:
    ds = [random.randint(1,100) for i in range(n)]
    return sorted(ds, reverse = True)

if __name__ == "__main__":
    print(question_17(7))

#bài 18
def question_18(s: str) -> str:
    return " ".join(s.split())
 
if __name__ == "__main__":
    print(question_18("  Python is   fun   "))
    print(question_18("  Hello word   "))

#bài 19
def question_19(x: int, n: int) -> bool:
    return x > n
        
if __name__ == "__main__":
    print(question_19(15, 10))
    print(question_19(5, 10))

#bài 20
from typing import Optional
def question_20() -> Optional[str]:
    s = input("Nhập giá trị từ bán phím: ")
    if s:
        return s
    else:
        return None
print(question_20())

#bài 21
def question_21(nums: list[int], target: int) -> tuple[int, int]:
    for i in range(len(nums)): #start = 0, len là có bnhieu số trong chuỗi
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return None
print( question_21([1,2,3,4,5],4))

#bài 22
def question_22(nums: list[int]) -> None:
    so_0 = nums.count(0)
    nums_moi = [i for i in nums if i != 0]
    nums_moi.extend([0]*so_0)
    return nums_moi
print(question_22([0,1,1]))

#bài 23
def question_23(nums: list[int]) -> bool:
   for i in nums:
        if nums.count(i) > 1:
            return True
        return False
print(question_23([1,1,2,3,4,5]))    
    
#bài 24
def question_24(nums: list[int]) -> int:
    return max(nums, key = nums.count)

print( question_24([2,3,2]))     

#bài 25
def question_25(nums: list[int]) -> list[int]:
    nums_new = sorted([i**2 for i in nums])
    return nums_new
print(question_25([-4,-1,0,3,10]))

#bài 26
import collections
def question_26(s: str) -> int:
    char_count = collections.Counter(s)
    length = 0
    odd_found = False 
    for count in char_count.values():
        length += (count // 2 )* 2
        if count % 2 == 1:
            odd_found = True
    if odd_found:
        length += 1
    return length
print(question_26("abccccdd"))

#bài 27
def question_27(strs: list[str]) -> str:
    tien_to = strs[0]
    for i in strs[1:]:
        while not i.startswith(tien_to):
            tien_to = tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to
print(question_27(["flower", "flow", "flight"]))

#bài 28
import collections
def question_28(s: str) -> dict[str, int]:
    dic_ky_tu = dict(collections.Counter(s))
    return dic_ky_tu
print(question_28("Hello"))

#bài 29
def question_29(nums: list[int]) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return nums[n//2]
    return (nums[n//2 -1 ] + nums[n //2]) /2
print(question_29([1, 3, 4, 2, 5]))
print(question_29([1, 2, 3, 4]))

#bài 30
def question_30(paragraph: str) -> dict[str, int]:
    tach_tu = paragraph.split()
    tu_dien = {i: tach_tu.count(i) for i in tach_tu}
    return tu_dien
print(question_30("hello world hello"))
print(question_30( "apple orange apple banana orange"))

#bài 31
from typing import List
import collections
def question_31(paragraph: str, n: int) -> List[str]:
    w_tach = paragraph.split()
    w_dem_xh = collections.Counter(w_tach)
    w_tong = len(w_tach)
    ds = []
    for word, count in w_dem_xh.items():
        if count / w_tong > 0.2:
            ds.append(word)
    return ds
print(question_31("apple apple banana orange orange apple", 2))

#bài 32
def question_32(nums: list[int]) -> tuple[list[int], list[int]]:
    chan = sorted( [i for i in nums if i %2 == 0], reverse = True)
    le = sorted([ i for i in nums if i % 2 != 0])
    return chan, le
print(question_32([4, 1, 3, 2, 7, 8, 5]))
print(question_32( [9, 12, 15, 6, 2, 14]))

#bài 33
def question_33(nums: list[int]) -> tuple[int, int]:
    if len(nums) < 5:
        return None 
    else:
        nums.sort(reverse = False)
        return nums[-2], nums[4]
print(question_33( [3, 1, 4, 5, 9, 2, 6, 8, 7]))
print(question_33( [1, 3, 2, 5]))

#bài 34
def question_34(s: str) -> int:
    danh_sach = []
    do_dai_max = 0
    for i in s:
        while i in danh_sach:
            danh_sach.pop(0)
        danh_sach.append(i)
        do_dai_max = max(do_dai_max, len(danh_sach))
    return do_dai_max
print(question_34("abcabcbb"))

#bài 35
def question_35(s: str) -> str:
    n = len(s)
    chuoi_dai = ""
    for i in range(n):
        for j in range(i+1, n):
            chuoi = s[i:j]
            if s.count(chuoi) > 1:
                if len(chuoi) > len(chuoi_dai):
                    chuoi_dai = chuoi
    return chuoi_dai
print(question_35("abcabcbb"))

#bài 36
import itertools
def question_36(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in itertools.permutations(nums)]
print(question_36([1,2,3]))

#bài 37
def question_37(s: str) -> bool:
    dic_ky_tu = {')':'(', '}':'{', ']':'['}
    ds_ngoac_mo = []
    for i in s:
        if i in dic_ky_tu.values():
            ds_ngoac_mo.append(i)
        elif i in dic_ky_tu:
            if ds_ngoac_mo and ds_ngoac_mo[-1] == dic_ky_tu[i]:
                ds_ngoac_mo.pop()
            else:
                return False
    return True if not ds_ngoac_mo else False
print(question_37("()"))

#bài 38
def question_38(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(question_38(2))

#bài 39
def question_39(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    gia_max = 0
    mua_min = prices[0]
    for i in prices[1:]:
        gia_max = max(gia_max, i - mua_min)
        mua_min = min(mua_min, i)
    return gia_max
print(question_39([6, 7, 8, 9, 20, 5]))







