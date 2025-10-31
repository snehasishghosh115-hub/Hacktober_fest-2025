nums = sorted(list(map(int, input().split())))
n = len(nums)
res = []
for i in range(n - 2):
    if i > 0 and nums[i] == nums[i - 1]: continue
    l, r = i + 1, n - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s == 0:
            res.append([nums[i], nums[l], nums[r]])
            l += 1; r -= 1
            while l < r and nums[l] == nums[l - 1]: l += 1
            while l < r and nums[r] == nums[r + 1]: r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1
print(res)
