#include <iostream>

using namespace std;

int n, k;
int memo[1000][1000];
int mod = 10007;

int combination (int n, int k) {
  // 파스칼 삼각형의 원리를 이용해서 combination 계산
  if (k == 0 || n == k) {
    return 1;
  } else if (memo[n][k] > 0){
    return memo[n][k];
  }
  else {
    memo[n][k] = (combination(n-1, k-1) + combination(n-1, k)) % mod;
    return memo[n][k];
  }
}

int main() {
  cin >> n >> k;

  cout << combination(n, k) % mod;
}