import copy
def solution(board):
    size = len(board)
    result = max(board[0])

    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    score_matrix = [[0 for col in range(4)] for row in range(size)]
    score_matrix[0] = copy.deepcopy(board[0])
    
    for i in range(1, size):
        for j in range(4):
            score_matrix[i][j] = board[i][j] + max(score_matrix[i-1][:j] + score_matrix[i-1][j+1:])
    return max(score_matrix[size - 1])