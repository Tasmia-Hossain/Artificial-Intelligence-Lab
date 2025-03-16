def heuristic(board):
    attacking_pair = 0
    nonattacking=0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pair += 1
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                nonattacking += 1
    print('Number of nonattacking pairs: ',nonattacking)
    return attacking_pair

n = int(input("Enter the number of queens: "))
#board = [6,1,5,7,4,3,8,1]
board = list(map(int, input(f"Enter {n} queen positions: ").split()))
print('Number of attacking pairs: ', heuristic(board))
print('Number of total unique pairs: ',(n*(n-1))/2)
