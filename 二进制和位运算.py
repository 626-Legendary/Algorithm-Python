# ==============================
# 二进制和位运算（8 位视角）
# ==============================

"""
位运算 vs 逻辑运算（一定要区分）：
位运算：对 二进制位 操作
逻辑运算：对 True / False 操作

位运算符：
&   按位与     两位都 1 才是 1
|   按位或     有一个 1 就是 1
^   按位异或   相同为 0，不同为 1
~   按位取反   0 ↔ 1（注意补码）
<<  左移       左移补 0（相当于 ×2）
>>  右移       算术右移（补符号位）
"""

# ==============================
# 工具函数：统一 8 位二进制显示
# ==============================
def bin8(x):
    """
    将整数按 8 位补码形式显示
    关键点：
    - Python int 没有固定位数
    - & 0xff 用来“截断”为 8 位
    """
    return format(x & 0xff, "08b")


print("========== 按位与 & ==========")
# &：两位都为 1 才是 1
num1 = 1   # 00000001
num2 = 1   # 00000001
print(f"num1 = {bin8(num1)}")
print(f"num2 = {bin8(num2)}")
print("num1 & num2 =", bin8(num1 & num2))  # 00000001
print()

num1 = 1   # 00000001
num2 = 2   # 00000010
print(f"num1 = {bin8(num1)}")
print(f"num2 = {bin8(num2)}")
print("num1 & num2 =", bin8(num1 & num2))  # 00000000
print()


print("========== 按位或 | ==========")
# |：有一个为 1 就是 1
num1 = 1
num2 = 2
print(f"num1 = {bin8(num1)}")
print(f"num2 = {bin8(num2)}")
print("num1 | num2 =", bin8(num1 | num2))  # 00000011
print()


print("========== 按位异或 ^ ==========")
# ^：相同为 0，不同为 1
num1 = 1
num2 = 1
print(f"num1 = {bin8(num1)}")
print(f"num2 = {bin8(num2)}")
print("num1 ^ num2 =", bin8(num1 ^ num2))  # 00000000
print()

num1 = 1
num2 = 2
print(f"num1 = {bin8(num1)}")
print(f"num2 = {bin8(num2)}")
print("num1 ^ num2 =", bin8(num1 ^ num2))  # 00000011
print()


print("========== 按位取反 ~ ==========")
# ~x = -x - 1（补码规则）
num1 = 1
print(f"num1     = {bin8(num1)}")
print(f"~num1    = {bin8(~num1)}")  # 11111110
print("说明：~00000001 = 11111110（8 位补码）")
print()


print("========== 左移 << ==========")
# 左移：低位补 0，相当于 ×2
num1 = 3  # 00000011
print(f"num1        = {bin8(num1)}")
print(f"num1 << 1   = {bin8(num1 << 1)}")  # 00000110
print(f"num1 << 2   = {bin8(num1 << 2)}")  # 00001100
print()


print("========== 右移 >> ==========")
# 右移：算术右移（补符号位）
num1 = -8
print(f"num1        = {bin8(num1)}")
print(f"num1 >> 1   = {bin8(num1 >> 1)}")  # 11111100
print()


print("========== 十进制 → 二进制（位扫描法） ==========")
"""
这是“教学用写法”，不是最快
目的：
- 理解每一位是怎么来的
- 理解掩码 & 和移位 >>
"""

num1 = 85  # 十进制 85
# 二进制：01010101
print("num1 =", num1)
print("bin(num1) =", bin(num1))
print("8 位补码  =", bin8(num1))

result = ""
for i in range(7, -1, -1):
    # 右移 i 位，再 & 1，取出当前位
    bit = (num1 >> i) & 1
    result += str(bit)

print("位扫描结果 =", result)
print()


print("========== 重要结论（笔记） ==========")
print("""
1. Python int 没有固定 8/32/64 位
2. 位运算结果本身是“无限位”的
3. 显示为 8 位，必须：
   - 使用掩码：& 0xff
   - 再用 format(..., '08b')
4. bin(x) 显示的是“数值”，不是“内存补码”
5. 教学 / 计组 / OS：一定要先规定“位宽”
""")
