#include <iostream>

using namespace std;

int w, h;
int memo[101][101][2][2]; 
// 3rd index - 0: from W, 1: from S
// 4th index - 0: can turn, 1: can't turn
int mod = 100000;

int main() {
  scanf("%d %d", &w, &h);

  for (int i = 2; i <= w; i++) {
    memo[i][1][0][0] = 1;
  }
  for (int i = 2; i <= h; i++) {
    memo[1][i][1][0] = 1;
  }

  for (int i = 2; i <= w; i++) {
    for (int j = 2; j <= h; j++) {
      memo[i][j][0][0] = (memo[i-1][j][0][0] + memo[i-1][j][0][1]) % mod;
      memo[i][j][0][1] = memo[i-1][j][1][0];
      memo[i][j][1][0] = (memo[i][j-1][1][0] + memo[i][j-1][1][1]) % mod;
      memo[i][j][1][1] = memo[i][j-1][0][0];
    }
  }
  int sum = memo[w][h][0][0] + memo[w][h][0][1] + memo[w][h][1][0] + memo[w][h][1][1];
  printf("%d\n", sum % mod);  
}
