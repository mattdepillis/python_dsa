"""
Given an unordered list of integers in the range of [1, n], where n is the length of the list + 2, find the two numbers that are missing from the current list of length n - 2.

TC: O(n) -- need to loop through the list n times to take care of every value
SC: O(1) -- sorts in-place
"""
def missing_numbers(nums):
  missing, sorted_to = [], 0

  for _ in range(2): nums.append(None)

  for _ in range(len(nums)):
    i = sorted_to

    while i < len(nums) - 1:
      if nums[i] is not None and nums[i] != i + 1:
        sorted_to = i
        break
      i += 1

    if nums[i] is None: continue
    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
  
  for i in range(len(nums)):
    if nums[i] is None: missing.append(i + 1)
  return missing


if __name__ == "__main__":
  # print(missing_numbers(
  #   [1, 15, 16, 17, 18, 19, 20, 21, 22, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  # )) # 1, 2

  print(missing_numbers(
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ))