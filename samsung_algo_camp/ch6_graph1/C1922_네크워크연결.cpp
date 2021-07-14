#include <cstdio>
#include <queue>
#include <vector>

using namespace std;
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > piii;
priority_queue<piii, vector<piii>, greater<piii> > pq;
int n, m;
int parent[1001];
int answer;

int find_set(int x) {
  if (parent[x] == x) return x;
  else 
    return parent[x] = find_set(parent[x]);
}

bool union_set(int x, int y) {
  int px = find_set(x);
  int py = find_set(y);
  
  if (px == py) 
    return false;
  
  parent[px] = py;
  return true;
}

int main() {
  scanf("%d", &n);
  scanf("%d", &m);

  for (int i = 0; i < m; i++) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    pq.push(piii(c, pii(a, b)));
  }

  for (int i = 1; i <= n; i++) {
    parent[i] = i;
  }

  int union_cnt = 0;
  while(!pq.empty()) {
    piii edge = pq.top(); pq.pop();
    int weight = edge.first;
    int x = edge.second.first;
    int y = edge.second.second;

    if(union_set(x, y)) {
      answer += weight;
      union_cnt++;
      // 경로를 알고 싶다면 union 성공시 완성된 트리에 엣지를 추가해주면 됨
    }
    if (union_cnt == n - 1) break; // 트리의 엣지 수는 node - 1
  }

  printf("%d\n", answer);
}

