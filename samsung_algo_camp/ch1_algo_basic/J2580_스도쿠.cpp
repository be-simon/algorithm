#include <iostream>

using namespace std;

int board[9][9];

void check_blank(int i, int j) {
  
}

int main() {
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      scanf("%d ", &board[i][j]);
    }
  }

  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      if (board[i][j] > 0) continue;

      // logic

    }
  }

  // print
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      printf("%d ", &board[i][j]);
    }
    printf("%\n");
  }
}