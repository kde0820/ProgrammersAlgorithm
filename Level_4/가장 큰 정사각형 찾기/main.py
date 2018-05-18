def findLargestSquare(board):
    answer = 0
    matrix = [[1 if x == 'O' else 0 for x in sub] for sub in board]   
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if matrix[i][j] == 0:
                continue
            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
            answer = max(answer, matrix[i][j])
    return answer**2

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))