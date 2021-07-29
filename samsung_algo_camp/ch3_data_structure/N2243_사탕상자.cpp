#include <iostream>
#define MAXN 1000000

int tree[1<<21];
int n;

int query(int node,  int s, int e, int l, int r) {
  if (r < s || e < l) 
    return 0;
  
  if (l <= s && e <= r) 
    return tree[node];
  
  int mid = (s + e) / 2;
  return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
  
}

void update(int node, int s, int e, int idx, int val) {
  if (idx < s || e < idx)
    return;
  
  tree[node] += val;
  if (s == e) return;
  
  int mid = (s + e) / 2;
  update(node * 2, s, mid, idx, val);
  update(node * 2 + 1, mid + 1, e, idx, val);
}

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n;i++) {
    int a, b, c;
    scanf("%d %d", &a, &b);
    if (a == 1) {
      int s = 1, e = MAXN;
      while (e - s > 0) {
        int mid = (s + e) / 2;
        int q = query(1, 1, MAXN, 1, mid);
        if (q < b)
          s = mid + 1;
        else 
          e = mid;
      }
      printf("%d\n", e);
      update(1, 1, MAXN, e, -1);
    } else if (a == 2) {
      scanf("%d", &c);
      update(1, 1, MAXN, b, c);
    }
  }
}