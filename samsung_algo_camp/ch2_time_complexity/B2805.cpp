#include <iostream>

using namespace std;

int n, m;
typedef long long LL;
LL trees[1000000];

bool is_cutting(LL h) {
  LL sum = 0;
  for (int i = 0; i < n; i++) {
    if (trees[i] > h)
      sum += trees[i] - h;
    if (sum >= m) return true;
  }
  return false;
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    scanf("%lld", trees + i);
  }

  // 이분 탐색
  LL bottom = 0;
  LL top = 1000000000;
  LL mid;
  LL answer = 0;

  while (bottom <= top) {
    mid = (bottom + top) / 2;
    if (is_cutting(mid)) {
      answer = max(answer, mid);
      bottom = mid + 1;
    }
    else 
      top = mid - 1;
  }

  cout << answer << endl;
}