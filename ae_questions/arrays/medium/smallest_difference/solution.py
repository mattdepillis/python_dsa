"""
Write a function that takes 2 non-empty arrays of integers and returns an array of 2 numbers (one from each array) whose absolute difference is the smallest. The number in the first array should appear first in the return array.
TC: O(nlog(n) + mlog(m)), where n is the length of array1 and m is the length of array2
SC: O(1)
"""
def smallest_difference(array1, array2):
  array1.sort(), array2.sort()

  smallest_diff, pair = float('inf'), []
  p1 = p2 = 0

  while p1 < len(array1) and p2 < len(array2):
    diff = abs(array1[p1] - array2[p2])
    if diff < smallest_diff:
      smallest_diff, pair = diff, [array1[p1], array2[p2]]

    if p1 + 1 == len(array1):
      p2 += 1
    elif p2 + 1 == len(array2):
      p1 += 1
    elif abs(array1[p1 + 1] - array2[p2]) > abs(array1[p1] - array2[p2 + 1]):
      p2 += 1
    elif p2 + 1 == len(array2) or abs(array1[p1 + 1] - array2[p2]) < abs(array1[p1] - array2[p2 + 1]):
      p1 += 1
    else:
      p1, p2 = p1 + 1, p2 + 1

  return pair


if __name__ == "__main__":
  # print(smallest_difference(
  #   [-1, 5, 10, 20, 28, 3],
  #   [26, 134, 135, 15, 17]
  # ))

  # print(smallest_difference(
  #   [-1, 5, 10, 20, 3],
  #   [26, 134, 135, 15, 17]
  # ))

  # print(smallest_difference(
  #   [240, 124, 86, 111, 2, 84, 954, 27, 89],
  #   [1, 3, 954, 19, 8]
  # ))

  print(smallest_difference(
    [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
    [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
  ))
