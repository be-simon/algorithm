#include <iostream>
#include <algorithm>

using namespace std;

int n;
int tree[1<<20];
typedef pair<int, int> pii;
pii player[500000];

bool compare(pii a, pii b) {
  return a.second < b.second;
}

int get_seg_sum(int node, int s, int e, int l, int r) {
  if (r < s || e < l) return 0;
  if (l <= s && e <= r) return tree[node];
  else {
    int mid = (s + e) / 2;
    return get_seg_sum(node * 2, s, mid, l, r) + get_seg_sum(node * 2 + 1, mid + 1, e, l, r);
  }
}

void update_seg_sum(int node, int s, int e, int idx, int val) {
  if (idx < s || e < idx) return ;
  tree[node] += val;
  
  if (s == e) return;
  else {
    int mid = (s + e) / 2;
    update_seg_sum(node * 2, s, mid, idx, val);
    update_seg_sum(node * 2 + 1, mid + 1, e, idx, val);
  }
}

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    player[i].first = i;
    scanf("%d", &player[i].second);
  }

  // power relabeling
  sort(player, player + n, compare);
  for (int i = 0; i < n; i++) {
    player[i].second = i + 1;
  }

  sort(player, player + n);
  for (int i = 0; i < n; i++) {
    int power = player[i].second;
    int cnt = get_seg_sum(1, 1, n, 1, power - 1);
    update_seg_sum(1, 1, n, power, 1);
    printf("%d\n", i - cnt + 1);
  }
}