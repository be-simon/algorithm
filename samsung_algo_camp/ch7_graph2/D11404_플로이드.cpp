#include <iostream>
#include <vector>
#define INF 100000000

using namespace std;

int n, m;
int cost[101][101];

int main() {
  cin >> n >> m;

  // init
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (i == j) cost[i][j] = 0;
      else cost[i][j] = INF;
    }
  }

  // input
  int a, b, c;
  for (int i = 1; i <= m; i++) {
    cin >> a >> b >> c;      
    cost[a][b] = min(cost[a][b], c);
  }

  // floyd-warshall
  for (int k = 1; k <= n; k++) {
    for(int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if(cost[i][j] > cost[i][k] + cost[k][j])
          cost[i][j] = cost[i][k] + cost[k][j];
      }
    }
  }

  // output
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (cost[i][j] == INF)
        cout << 0 << " ";
      else  
        cout << cost[i][j] << " ";
    }
    cout << "\n";
  }
  
}