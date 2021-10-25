#include <iostream>

#define MAX 100

using namespace std;

int n, m;
int dp[MAX][MAX * MAX + 1];
int mem[MAX];
int cost[MAX];

int main() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%d", mem + i);
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", cost + i);
  }

  int answer = -1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= MAX * MAX; j++) {
      if (i == 0) 
        dp[i][j] = cost[i] <= j ? mem[i] : 0;
      else if (cost[i] <= j)
        dp[i][j] = max(dp[i-1][j-cost[i]] + mem[i], dp[i-1][j]);
      else
        dp[i][j] = dp[i-1][j];

      if (dp[i][j] >= m) {
        answer = answer == -1 ? j : min(answer, j);
      }
    }
  }
  
  printf("%d\n", answer);
}