class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r,c = len(board),len(board[0])
        m = {'1','2','3','4','5','6','7','8','9'}
        r_idx = {}
        c_idx = {}
        boxes = {}
        row = 0
        col = 0
        row_count = 0
        col_count = 0
        restart_col = 0
        restart_row = 0
        idx = 1
        while True:
            if row < len(board):
                if row < (restart_row + 3):
                    while col < (restart_col + 3):
                        #box logic
                        if boxes.get(idx):
                            if board[row][col] in m or board[row][col] == '.':
                                if board[row][col] not in tuple(boxes[idx]) or board[row][col] == '.' :
                                    boxes[idx] = boxes[idx] + [board[row][col]]
                                else:
                                    return False
                            else:
                                return False
                        else:
                            boxes[idx] = [board[row][col]]
                        #row_logic
                        if r_idx.get(row):
                            if board[row][col] in m or board[row][col] == '.':
                                if board[row][col] not in tuple(r_idx[row]) or board[row][col] == '.' :
                                    r_idx[row] = r_idx[row] + [board[row][col]]
                                else:
                                    return False
                            else:
                                return False
                        else:
                            r_idx[row] = [board[row][col]]
                        #column_logic
                        if c_idx.get(col):
                            if board[row][col] in m or board[row][col] == '.':
                                if board[row][col] not in tuple(c_idx[col]) or board[row][col] == '.' :
                                    c_idx[col] = c_idx[col] + [board[row][col]]
                                else:
                                    return False
                            else:
                                return False
                        else:
                            c_idx[col] = [board[row][col]]

                        col += 1
                    col = restart_col
                    row += 1
                    row_count += 1
                    col_count += 1

                else:
                    if row_count == 9 and col_count == 9: # 3 boxes over
                        restart_row = row
                        col = 0
                        row_count = 0
                        col_count = 0
                        restart_col = col
                        idx += 1
                    else:
                        restart_col = col_count
                        col = col_count
                        row = restart_row
                        idx += 1
            else:
                if row_count == 9 and col_count == 9:
                    return True
                restart_col = col_count
                col = col_count
                row = restart_row 
                idx += 1
       
            
                 





