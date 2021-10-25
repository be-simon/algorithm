#include <iostream>
#include <queue>
#include <vector>
#include <string.h>
#define INF 100000000

using namespace std;

typedef struct Node {
  int d;
  int v;
  int c;
} Node;

struct cmp {
	bool operator()(Node a, Node b) {
		return a.d > b.d;
	}
};

int T, N, M, K;
int dp[101][10001];

int main() {
  scanf("%d", &T);
  while (T--) {
    vector<Node> g[10001];
    scanf("%d %d %d", &N, &M, &K);
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= 100; i++) {
      for (int j = 0; j <= 1000; j++) {
        dp[i][j] = INF;
      }
    }
    for (int i = 0; i < K; i++) {
      int u, v, c, d;
      scanf("%d %d %d %d", &u, &v, &c, &d);
      g[u].push_back({d, v, c});
    }

    priority_queue<Node, vector<Node>, cmp> pq;
    dp[1][0] = 0;
    pq.push({0, 1, 0});
    
    while (!pq.empty()) {
      int d, cur, c;
      d = pq.top().d;
      cur = pq.top().v;
      c = pq.top().c;
      pq.pop();
      
      if (cur == N) break;

      if (dp[cur][c] < d) continue;

      for (Node adn : g[cur]) {
        int ad = adn.v;
        int adc = adn.c;
        int add = adn.d;

        int nc = c + adc;
        int nd = d + add;

        if (nc > M) continue;

        if (nd < dp[ad][nc]) {
          for (int i = nc; i <= M; i++) {
            if (nd < dp[ad][i])
              dp[ad][i] = nd;
          }
          dp[ad][nc] = nd;
          pq.push({nd, ad, nc});
        }
      }
    }

    if (dp[N][M] == INF)
      printf("Poor KCM\n");
    else printf("%d\n", dp[N][M]);
  }
}