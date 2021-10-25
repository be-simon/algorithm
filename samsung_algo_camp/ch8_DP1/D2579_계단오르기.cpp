#include <iostream>

using namespace std;

int n ;
int dp[300][2];

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int cur;
    cin >> cur;

    if (i == 0) {
      dp[i][0] = cur;
    } else if(i == 1) {
      dp[i][0] = dp[i-1][0] + cur;
      dp[i][1] = cur;
    } else {
      dp[i][0] = dp[i-1][1] + cur;
      dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + cur;
    } 
  }

  cout << max(dp[n-1][0], dp[n-1][1]);
}