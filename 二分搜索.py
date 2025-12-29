# 二分查找算法总结
# 1. 在有序数组中确定 num 是否存在                  -> exist()
# 2. 在有序数组中找 ≥ num 的最左位置 (lower bound)   -> findLeft()
# 3. 在有序数组中找 ≤ num 的最右边位置 (upper bound) -> findRight()
# 4. 二分搜索不一定发生在有序数组上 (寻找峰值)       -> findPeakElement()

# 时间复杂度均为 O(logN)

import math

# ==========================
# 1. 判断 num 是否存在
# ==========================
def exist(arr, num):
    n = len(arr)
    if n == 0:
        return False

    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] < num:
            l = mid + 1
        elif arr[mid] > num:
            r = mid - 1
        else:
            return True
    return False


# ==========================
# 2. 找 ≥ num 的最左位置
# 思路：命中 >= 时记录答案并继续往左缩 r
# ==========================
def findLeft(arr, num):
    res = -1
    n = len(arr)
    if n == 0 or arr[-1] < num:
        return res  # 越界情况：最大值 < num

    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] >= num:
            res = mid  # 可能是答案，但往左看看
            r = mid - 1
        else:
            l = mid + 1
    return res


# ==========================
# 3. 找 ≤ num 的最右位置
# 思路：命中 <= 时记录答案并继续往右缩 l
# ==========================
def findRight(arr, num):
    res = -1
    n = len(arr)
    if n == 0 or arr[0] > num:
        return res  # 越界情况：最小值 > num

    l, r = 0, n - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if arr[mid] <= num:
            res = mid  # 可能是答案；向右继续找更大的满足条件
            l = mid + 1
        else:
            r = mid - 1
    return res


# ==========================
# 4. 寻找峰值 (Peak Element)
# LeetCode 162
# 核心逻辑：通过 mid 与 mid+1 比较决定峰值一定在哪侧
# ==========================
def findPeakElement(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return n - 1

    l, r = 1, n - 2
    while l < r:
        mid = l + ((r - l) >> 1)
        # 如果右边比 mid 大，则峰一定在右侧
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l  # l == r，为峰值位置


# ==========================
# 测试运行
# ==========================
if __name__ == "__main__":
    print("========== TEST ==========")

    arr1 = [1,2,3,4,5,6,7,8,9,10]
    print("exist(arr1, 6):", exist(arr1, 6))

    arr2 = [1,2,3,4,5,6,8,9,10]
    print("findLeft(arr2, 7):", findLeft(arr2, 7))

    arr3 = [1,3,4,4,4,7,9,10]
    print("findRight(arr3, 4):", findRight(arr3, 4))

    arr4_1 = [1,2,3,1]
    arr4_2 = [1,2,1,3,5,6,4]
    print("findPeakElement(arr4_1):", findPeakElement(arr4_1))
    print("findPeakElement(arr4_2):", findPeakElement(arr4_2))
