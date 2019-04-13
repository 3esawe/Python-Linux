def print_paths(board):
    output_list = []
    temp_str_list = []
    search(0,0,board,temp_str_list,output_list)
    return output_list    

def search(i,j,board,temp_str_list,output_list):
    rows = len(board)
    cols = len(board[0])
    if i > rows - 1 or j > cols -1:
        return
    temp_str_list.append(board[i][j])
    if i == rows - 1 and j == cols - 1:
        output_list.append("".join(temp_str_list))
        temp_str_list.pop()
        return
  
    search(i+1,j,board,temp_str_list,output_list); # Search Down
    search(i,j+1,board,temp_str_list,output_list); # Search Right
    temp_str_list.pop() # Un-Mark