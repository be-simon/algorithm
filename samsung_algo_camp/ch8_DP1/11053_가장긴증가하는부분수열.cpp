#include <cstdio>
#include <bits/stdc++.h>

using namespace std;

int n;
int arr[1010];
int dp[1010];
int answer;

int main () {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
    
    int maxv = 0;
    for (int j = i-1; j >= 0; j--) {
      if (arr[j] < arr[i]) {
        maxv = max(maxv, dp[j]);
      }
    }
    dp[i] = maxv + 1;
    answer = max(answer, dp[i]);
  }

  printf("%d\n", answer);
}
