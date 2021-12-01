nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    start = 0
    end = len(nums) - 1
    mid = end - start // 2

    while len(nums) > 1:
        if nums[mid] == target:
            print(mid)
        elif nums[mid] > target:
            start = 0
            end = mid
        elif nums[mid] < target:
            start = mid
            end = length[nums] - 1

        else:
            print (-1)

print(search(nums,target))