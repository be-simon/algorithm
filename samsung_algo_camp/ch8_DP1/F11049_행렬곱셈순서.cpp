#include <cstdio>

using namespace std;

typedef long long ll;
int n;
ll dp[500][500];
ll mat[501];


int recur(int s, int e) {
  if (s == e)
    return 0;
  else if (e - s == 1) 
    return mat[s] * mat[e] * mat[e + 1];
  else if (dp[s][e] > 0) 
    return dp[s][e];
  else {
    int m = 0;
    for (int k = s; k < e; k++) {
      int a = recur(s, k) + recur(k + 1, e) + mat[s] * mat[k + 1] * mat[e + 1];
      if (m == 0 || m > a)
        m = a;
    }
    dp[s][e] = m;
    return m;
  }
}

int main() {
  ll r,c;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    scanf ("%lld %lld", &r, &c);
    if (i == 0)
      mat[i] = r;
    mat[i + 1] = c;
  }

  printf("%lld\n", recur(0, n-1));
}