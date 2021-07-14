#include <cstdio>
#include <vector>
#include <queue>
#define INF 1000000000
using namespace std;

int n, m;
int g[501][501];
int d[501][501];

// 플로이드 와샬
void floyd_warshall() {
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      d[i][j] = g[i][j];
    }
  }

  for(int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (d[i][j] > d[i][k] + d[k][j])
          d[i][j] = 1;
      }
    }
  }
}

int main() {
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= n; i++) 
    for (int j = 1; j <= n; j++) 
      if (i == j) g[i][j] = 0;
      else g[i][j] = INF;


  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    g[a][b] = 1;
  }

  floyd_warshall();

  int answer = 0;
  for (int i = 1; i <= n; i++) {
    int sum = 0;
    for (int j = 1; j <= n; j++) {
      if (d[i][j] == 1) sum += d[i][j];
      if (d[j][i] == 1) sum += d[j][i];
    }
    if (sum == n - 1) answer++;
  }

  printf("%d\n", answer);
}