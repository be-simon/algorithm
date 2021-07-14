#include <iostream>

using namespace std;

int n, m, k;
typedef long long ll;
ll arr[1000000];
ll tree[1<<21];

ll get_sum(int node, int s, int e, int l, int r) {
  if (r < s || e < l) return 0;
  else if (l <= s && e <= r) return tree[node];
  else {
    int mid = (s + e) / 2;
    return get_sum(node * 2, s, mid, l, r) + get_sum(node * 2 + 1, mid + 1, e, l, r);
  }
}

void update_tree(int node, int s, int e, int i, ll v) {
  if (i < s || e < i) return;
  if (s == e) 
    tree[node] = v;
  else {
    int mid = (s + e) / 2;
    update_tree(node * 2, s, mid, i, v);
    update_tree(node * 2 + 1, mid + 1, e, i, v);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
  }
}

int main() {
  scanf("%d %d %d", &n, &m, &k);
  for (int i = 0; i < n; i ++) {
    scanf("%lld ", arr + i);
  }

  for (int i = 0; i < n; i++) {
    update_tree(1, 1, n, i + 1, arr[i]);
  }

  int a, b;
  ll c;
  for (int i = 0; i < m + k; i++) {
    scanf("%d %d %lld", &a, &b, &c);
    if (a == 1) {
      update_tree(1, 1, n, b, c);
    } else if (a == 2) {
      printf("%lld\n", get_sum(1, 1, n, b, static_cast<int>(c)));
    }
  }
}