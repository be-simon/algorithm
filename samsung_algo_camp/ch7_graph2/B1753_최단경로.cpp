#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

#define INF 1000000000
#define MAX 20001

using namespace std;

int V, E, K;
typedef pair<int, int> pii; // w, v
vector<pii> g[MAX];
int d[MAX];


int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  cin >> V >> E;
  cin >> K;

  memset(d, -1, sizeof(d));

  for (int i = 0; i < E; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    g[u].push_back(pii(v, w));
  }

  priority_queue<pii, vector<pii>, greater<pii> > pq;
  pq.push(pii(0, K));
  d[K] = 0;
  while (!pq.empty()) {
    int cur = pq.top().second; pq.pop();
    for (pii next : g[cur]) {
      int nv = next.first;
      int nw = next.second;
      int nd = d[cur] + nw;
      if ((d[nv] == -1) || (d[nv] > nd)) {
        d[nv] = nd;
        pq.push(pii(nd, nv));
      }
    }
  }

  for (int i = 1; i <= V; i++) {
    if (d[i] == -1) cout << "INF\n";
    else cout << d[i] << "\n";
  }
}

