if __name__ == '__main__':
    n = int(input())
    nums = []
    i = 0
    while i < n:
        nums.append(i)
        i = i + 1
    for num in nums:
        print(num ** 2)