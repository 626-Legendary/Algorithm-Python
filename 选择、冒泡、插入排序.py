"""
本节内容：基础排序算法笔记

一句话总结：
1. 选择排序（Selection Sort）：i~n-1范围上，找到最小值并放在i位置，然后i+1~n-1范围上继续
2. 冒泡排序（Bubble Sort）：0~i范围上，相邻位置较大的数滚下去，最大值最终来到i位置，然后0~i-1范围上继续
3. 插入排序（Insertion Sort）：0~i范围上已经有序，新来的数从右到左滑到不再小的位置插入，然后继续
"""

arr = [37, 12, 89, 45, 3, 67, 12, 90, 24, 56, 8, 41]

# -----------------------------
# 选择排序
# -----------------------------
def selectionSort(arr):
    """
    选择排序（Selection Sort）
    思想：
    第 i 轮，从未排序区间 arr[i ~ n-1] 中找最小值，
    然后把它放到位置 i 上
    """
    print("==========选择排序==========")
    print("原始数组：", arr)

    n = len(arr)
    if n < 2:
        return

    # 外层循环：控制第 i 轮排序
    # 这里 n 也可以写作 n - 1
    for i in range(n):

        # 假设当前位置 i 就是最小值的下标
        minIndex = i

        # 内层循环：在未排序区间 [i+1, n-1] 中寻找真正的最小值
        for j in range(i + 1, n):

            # 如果发现更小的元素
            if arr[j] < arr[minIndex]:
                # 更新最小值的下标
                minIndex = j

        # 将第 i 位元素 与 找到的最小值元素 进行交换
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    print("排序后数组：", arr)

# -----------------------------
# 冒泡排序
# -----------------------------
def bubbleSort(arr):
    print("==========冒泡排序==========")
    print("原始数组：", arr)
    n = len(arr)
    if n < 2:
        return

    # 外层循环控制轮数
    for i in range(n - 1):  # 最后一轮无需比较，i范围到 n-2 即可
        # 内层循环控制相邻元素交换
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("排序后数组：", arr)

# -----------------------------
# 插入排序
# -----------------------------
def insertionSort(arr):
    print("==========插入排序==========")
    print("原始数组：", arr)
    n = len(arr)
    if n < 2:
        return

    # 从第二个元素开始，依次插入到前面已经排序的区间
    for i in range(1, n):
        j = i
        # 当前元素从右向左滑动，直到遇到不再小的元素
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    print("排序后数组：", arr)


# -----------------------------
# 测试
# -----------------------------
# 可以分别测试
selectionSort(arr.copy())
# bubbleSort(arr.copy())
# insertionSort(arr.copy())
