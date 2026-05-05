class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            for column in range(columns):
                if self.dfs(board,row,column,word,0):
                    return True
        return False
    def dfs(self,board,row,column,word,word_index):
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
            return False
        if board[row][column] != word[word_index]:
            return False
        if word_index == len(word) - 1:
            return True
        org_char = board[row][column]
        board[row][column] = "#"

        found = (self.dfs(board, row-1, column, word, word_index+1) or    # Up
             self.dfs(board, row+1, column, word, word_index+1) or    # Down  
             self.dfs(board, row, column-1, word, word_index+1) or    # Left
             self.dfs(board, row, column+1, word, word_index+1))  
        
        board[row][column] = org_char
        return found