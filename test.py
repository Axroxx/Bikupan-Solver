def find_neighbors(num):
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17, 18],
        [19, 20, 21],
        [22, 23, 24, 25],
    ]

    def get_position(num):
        for row_idx, row in enumerate(grid):
            if num in row:
                return row_idx, row.index(num)
        return None

    def in_bounds(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    def get_adjacent(row, col):
        adjacent = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if in_bounds(new_row, new_col):
                adjacent.append(grid[new_row][new_col])
        return adjacent

    def spiral_traversal(num):
        visited = set()
        queue = [(0, num)]  # The first element is the level, the second element is the number

        while queue:
            level, curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                row, col = get_position(curr)
                neighbors = get_adjacent(row, col)

                # Sort neighbors by their distance to the current number
                neighbors = sorted(
                    neighbors,
                    key=lambda neighbor: (abs(neighbor - curr), -get_position(neighbor)[0])
                )

                for neighbor in neighbors:
                    queue.append((level + 1, neighbor))

        return [num for _, num in sorted(list(visited), key=lambda x: x[0])]

    return spiral_traversal(num)


# Example usage:
starting_number = 13
result = find_neighbors(starting_number)
print(result)
