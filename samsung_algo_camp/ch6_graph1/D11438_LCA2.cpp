#include <iostream>
#include <vector>
#include <queue>
#define MAX_POW 18

using namespace std;

int n, m;
vector<int> g[100010];
int depth[100010];
int parent[MAX_POW][100010];

// bfs 방식으로 노드들의 depth를 구한다.
void cal_depth() {
  int visit[100010];
  queue<int> q;
  q.push(1);
  visit[1] = 1;
  for (int cur_depth = 0; !q.empty(); cur_depth++) {
    int qsize = q.size();
    for (int i = 0; i < qsize; i++) {
      int cur = q.front(); q.pop();
      depth[cur] = cur_depth;
      for (int next : g[cur]) {
        if (visit[next]) continue;
        q.push(next);
        visit[next] = 1;
        parent[0][next] = cur;
      }
    }
  }
}

// 노드들의 2^n 부모들을 구한다.
void cal_parent() {
  for (int i = 1; i < MAX_POW; i++)
    for (int j = 1; j <= n; j++) 
      parent[i][j] = parent[i-1][parent[i-1][j]]; // 2^k = 2^(k-1) + 2^(k-1)
}

// LCA를 구한다.
int lca(int a, int b) { // a가 더 깊은 것으로 취급할 것
  int temp;
  if (depth[a] < depth[b]) {
    temp = a;
    a = b;
    b = temp;
  }

  // b의 depth에 맞춰주기
  temp = depth[a] - depth[b];
  for (int i = 0; i < MAX_POW; i++) {
    int bit = (1 << i);
    if ((temp & bit) == bit) {
      a = parent[i][a];
    }
  }
  if (a == b) return a;
  
  for (int i = MAX_POW - 1; i >= 0; i--) {
    if (parent[i][a] != parent[i][b]) {
      a = parent[i][a];
      b = parent[i][b];
    }
  }
  return parent[0][a];
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  cin >> n;
  for (int i = 0 ; i < n-1; i++) {
    int s, e;
    cin >> s >> e;
    g[s].push_back(e);
    g[e].push_back(s);
  }

  cal_depth();
  cal_parent();
  
  cin >> m;
  for (int i = 0; i < m;  i++) {
    int a, b;
    cin >> a >> b;
    cout << lca(a, b) << "\n";
  }
}