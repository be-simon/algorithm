#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int n, m;
int in[32001];
vector<int> g[32001];
queue<int> q;

int main() {
  scanf("%d %d", &n, &m);
  int a, b;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &a, &b);
    in[b]++;
    g[a].push_back(b);
  }

  // topological sorting
    // indegree가 0인 노드 출력
    // indegree 배열 값 갱신
    // 반복
  for (int i = 1; i <= n; i++) {
    if (in[i] == 0) {
      q.push(i);
      printf("%d ", i);
    }
  }
  
  while(!q.empty()) {
    int cur = q.front(); q.pop();
    for (int node : g[cur]) {
      in[node]--;
      if (in[node] == 0) {
        q.push(node);
        printf("%d ", node);
      }
    }
  }
}
