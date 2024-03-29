"""
Write a function that takes a list of Cartesian coordinates and returns the number of squares that can be formed from these coordinates.

TC: O(n^2) -- need to iterate through the list roughly n^2 times (for each element in list, try all combos with subsequent numbers)
SC: O(n) -- could store linearly-proportional number of square values, and store 2 to 3 possible pair values per generated pair.
"""

def generate_possible_pairs(one, two, delta_x, delta_y, slope):
  """ Generates the possible pairs for a given two points based on the slope of the line they form. """

  if slope == "undefined":
    possible_points = [
      [
        [one[0] + delta_y, one[1]],
        [two[0] + delta_y, two[1]]
      ],
      [
        [one[0] - delta_y, one[1]],
        [two[0] - delta_y, two[1]]
      ]
    ]
  elif slope == "zero":
    possible_points = [
      [
        [one[0], one[1] + delta_x],
        [two[0], two[1] + delta_x]
      ],
      [
        [one[0], one[1] - delta_x],
        [two[0], two[1] - delta_x]
      ]
    ]
  else:
    possible_points = [
      [
        [one[0] + abs(delta_y), one[1] + abs(delta_x)],
        [two[0] + abs(delta_y), two[1] + abs(delta_x)]
      ],
      [
        [one[0] - abs(delta_y), one[1] - abs(delta_x)],
        [two[0] - abs(delta_y), two[1] - abs(delta_x)]
      ]
    ]
    # if two == [-4, 2]: print('pp', possible_points)
    possible_points.append([
      [(one[0] + possible_points[0][1][0]) // 2, (one[1] + possible_points[0][1][1]) // 2],
      [(one[0] + possible_points[1][1][0]) // 2, (one[1] + possible_points[1][1][1]) // 2]
    ])

  return possible_points


def count_squares(points):
  """ Generates a list representing all valid squares that can be formed from the provided Cartesian coordinates. """
  squares = []
  
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      delta_x = points[j][0] - points[i][0]
      delta_y = points[j][1] - points[i][1]

      if delta_y == 0:
        possible_pairs = generate_possible_pairs(points[i], points[j], delta_x, delta_y, "zero")
      elif delta_x == 0:
        possible_pairs = generate_possible_pairs(points[i], points[j], delta_x, delta_y, "undefined")
      else:
        possible_pairs = generate_possible_pairs(points[i], points[j], delta_x, delta_y, "")
      
      # iterate through possible pairs
      for pair in possible_pairs:
        if points[i] in pair or points[j] in pair: continue
        if pair[0] in points and pair[1] in points:
          square = [points[i], points[j]] + pair
          square.sort()
          if not square in squares: squares.append(square)

  print(squares)
  return len(squares)

if __name__ == "__main__":
  print(count_squares([
    [1, 1],
    [0, 0],
    [-4, 2],
    [-2, -1],
    [0, 1],
    [1, 0],
    [-1, 4]
  ]))