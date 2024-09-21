from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # This can be solved using BFS
        # The queue used for the BFS will contain different board states

        # The entire board state can be respresented as a node.
        # While the adjacent nodes are different board states made by making a single change to the current board state.
        
        # Psuedocode
        # while q:
        #     v = q.popleft() 
            # for all adjacent board states, v:
                # if the board state is the solution, end the loop
                # else if the board state, u, has not been made:
                    # q.append(u)
                        # You will also need to add the number of moves for the board state
                    # visited.append(u)

        q = deque()
        visited = set()
        target_node = (1,2,3,4,5,0)
        start_coord = self.find_zero(board)
        moves = 0
        q.append((start_coord, board, moves))
        node = tuple(board[0] + board[1])
        visited.add(node)
        directions = [
            (0, 1), # move right
            (0, -1), # move left
            (1, 0), # move down
            (-1, 0), # move up
        ]
        while q:
            current_coord, current_board, current_moves = q.popleft()
            current_node = tuple(current_board[0] + current_board[1])
            
            if target_node == current_node:
                return current_moves
            
            # This enumerates all the "adjacent" board states
            for direction in directions:
                next_coord = (current_coord[0] + direction[0], current_coord[1] + direction[1])
                if not self.check_bounds(next_coord, board):
                    continue
                next_board = [list(current_board[0]), list(current_board[1])]
                self.swap_tiles(next_board, current_coord[0], current_coord[1], next_coord[0], next_coord[1])
                visited_key = tuple(next_board[0] + next_board[1])
                if not visited_key in visited:
                    visited.add(visited_key)
                    q.append((next_coord, next_board, current_moves + 1))
        return -1
    
    def find_zero(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)

    def swap_tiles(self, board, current_row, current_col, next_row, next_col):
        """
        simpler swap to understand what's happening
        a = 1
        b = 2

        a, b = b, a
        """
        board[current_row][current_col], board[next_row][next_col] = \
            board[next_row][next_col], board[current_row][current_col]

    def check_bounds(self, coords, board):
        return coords[0] >= 0 and coords[0] < len(board) and coords[1] >= 0 and coords[1] < len(board[0])