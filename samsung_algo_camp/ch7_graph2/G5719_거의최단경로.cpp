#include <cstdio>
#include <queue>
#include <vector>
#include <string.h>

#define MAXN 500

using namespace std;

typedef pair<int, int> pii; // w, v
int n, m;
int g[MAXN][MAXN];
int dist[MAXN];
vector<int> from[MAXN];
bool visit[MAXN];

void init() {
  memset(visit, 0, sizeof(visit));
  memset(g, 0, sizeof(g));
  for (int i = 0; i < MAXN; i++) 
    from[i].clear();
}

void dijkstra(int s, int d, bool check) { // check 면 경로까지 탐색
  memset(dist, -1, sizeof(dist));
  priority_queue<pii, vector<pii>, greater<pii> > pq;
  pq.push(pii(0, s));

  dist[s] = 0;
  while(!pq.empty()) {
    int cur = pq.top().second; 
    int cost = pq.top().first;
    pq.pop();

    if (dist[cur] != -1 && dist[cur] < cost) continue;

    for (int i = 0; i < n; i++) {
      if (g[cur][i] > 0) {
        int nd = cost + g[cur][i];
        if (dist[i] == -1 || dist[i] > nd) {
          if (check) {
            from[i].clear();
            from[i].push_back(cur);
          }
          dist[i] = nd;
          pq.push(pii(nd, i));
        }   
        else if(dist[i] == nd && check) {
          from[i].push_back(cur);
        }
      }
    }
  }
}

void remove_path(int d) {
  queue<int> q;
  q.push(d);
  visit[d] = 1;

  while(!q.empty()) {
    int cur = q.front(); q.pop();
    
    for (int f : from[cur]) {
      g[f][cur] = 0;
      if (visit[f]) continue;
      q.push(f);
      visit[f] = 1;
    }
  }
}

int main() {
  while(true) {
    scanf("%d %d", &n, &m);
    if (!n && !m) return 0;

    int s, d;
    scanf("%d %d", &s, &d);
    for (int i = 0 ; i < m; i++) {
      int u, v, p;
      scanf("%d %d %d", &u, &v, &p);
      g[u][v] = p;
    }

    dijkstra(s, d, 1);
    remove_path(d);
    dijkstra(s, d, 0);

    printf("%d\n", dist[d]);
    
    init();
  }
}