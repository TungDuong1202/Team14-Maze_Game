#include <iostream>
using namespace std;

char board[3][3] = { {' ', ' ', ' '}, 
                     {' ', ' ', ' '}, 
                     {' ', ' ', ' '} };
char currentPlayer = 'X';

void drawBoard() {
    cout << "-------------" << endl;
    for (int i = 0; i < 3; ++i) {
        cout << "| ";
        for (int j = 0; j < 3; ++j) {
            cout << board[i][j] << " | ";
        }
        cout << endl << "-------------" << endl;
    }
}

bool checkWin(char player) {
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == player && board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return true;
        if (board[0][i] == player && board[0][i] == board[1][i] && board[1][i] == board[2][i])
            return true;
    }
    if (board[0][0] == player && board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return true;
    if (board[0][2] == player && board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return true;
    return false;
}

bool checkDraw() {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ')
                return false;
        }
    }
    return true;
}

int evaluate() {
    if (checkWin('X')) return 10;
    else if (checkWin('O')) return -10;
    return 0;
}

int minimax(bool isMaximizing) {
    int score = evaluate();
    if (score != 0) return score;
    if (checkDraw()) return 0;

    if (isMaximizing) {
        int best = -1000;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (board[i][j] == ' ') {
                    board[i][j] = 'X';
                    best = max(best, minimax(false));
                    board[i][j] = ' ';
                }
            }
        }
        return best;
    } else {
        int best = 1000;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (board[i][j] == ' ') {
                    board[i][j] = 'O';
                    best = min(best, minimax(true));
                    board[i][j] = ' ';
                }
            }
        }
        return best;
    }
}

void bestMove() {
    int bestVal = -1000;
    int bestMoveRow = -1;
    int bestMoveCol = -1;

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ') {
                board[i][j] = 'X';
                int moveVal = minimax(false);
                board[i][j] = ' ';
                if (moveVal > bestVal) {
                    bestMoveRow = i;
                    bestMoveCol = j;
                    bestVal = moveVal;
                }
            }
        }
    }

    board[bestMoveRow][bestMoveCol] = 'X';
}

int main() {
    bool gameEnded = false;

    while (!gameEnded) {
        drawBoard();

        if (currentPlayer == 'X') {
            bestMove();
            if (checkWin('X')) {
                drawBoard();
                cout << "Player X wins!" << endl;
                gameEnded = true;
            } else if (checkDraw()) {
                drawBoard();
                cout << "It's a draw!" << endl;
                gameEnded = true;
            }
            currentPlayer = 'O';
        } else {
            int row, col;
            cout << "Player O, enter row (0-2) and column (0-2): ";
            cin >> row >> col;

            if (row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ') {
                cout << "Invalid move. Try again." << endl;
                continue;
            }

            board[row][col] = 'O';

            if (checkWin('O')) {
                drawBoard();
                cout << "Player O wins!" << endl;
                gameEnded = true;
            } else if (checkDraw()) {
                drawBoard();
                cout << "It's a draw!" << endl;
                gameEnded = true;
            }
            currentPlayer = 'X';
        }
    }

    return 0;
}

