#include <cstdio>
#include <vector>

#define MAX 1000010
#define PIV (1<<20)

using namespace std;

int n, answer;
int seq[MAX]; // seq vals
int dp[MAX];
int tree[PIV * 2];

void update(int idx, int v) {
  idx += PIV;
  tree[idx] = v;
  idx /= 2;
  while (idx > 0) {
    tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1]);
    idx /= 2;
  }
}

int query(int l, int r) { 
  l += PIV;
  r += PIV;
  int ret = 0;
  while (l <= r) {
    if (l % 2 == 1) ret = max(ret, tree[l++]);
    if (r % 2 == 0) ret = max(ret, tree[r--]);
    l /= 2;
    r /= 2;
  }
  
  return ret;
}

int main() {
  scanf("%d", &n);
  
  for (int i = 0; i < n; i++) {
    scanf("%d", &seq[i]);
    
    dp[i] = query(1, seq[i] - 1) + 1;
    answer = max(answer, dp[i]);
    update(seq[i], dp[i]);
  }

  printf("%d\n", answer);
}