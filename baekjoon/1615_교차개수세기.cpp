#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;
typedef long long L;
int n, m;
L tree[1<<12];
vector<pii> g;

L query(int node, int s, int e, int l, int r) {
  if (r < s || e < l) return 0;
  else if (l <= s && e <= r) return tree[node];
  else {
    int mid = (s + e) / 2;
    return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
  }
}

void update(int node, int s, int e, int idx) {
  if (idx < s || e < idx) return;
  tree[node] += 1;
  if (s == e) return;
  else {
    int mid = (s + e) / 2;
    update (node * 2, s, mid, idx);
    update (node * 2 + 1, mid + 1, e, idx);
  }
}

int main() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < m; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    g.push_back(pii(a, b));
  }

  sort(g.begin(), g.end());

  L answer = 0;
  for (int i = 0; i < m; i++) {
    int v = g[i].second;
    answer += query(1, 1, n, v + 1, n);
    update(1, 1, n, v);
  }

  printf("%lld\n", answer);
}