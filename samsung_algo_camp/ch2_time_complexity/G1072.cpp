#include <iostream>

using namespace std;

long x, y;

int main() {
  cin >> x >> y;
  long z;

  z = y * 100 / x;
  if (z == 100 || z == 99) {
    cout << -1 << endl;
    return 0;
  }

  // 이분탐색
  long bottom = 1, top = 1000000000, mid;
  long answer = 1000000000;
  while (bottom <= top) {
    mid = (bottom + top) / 2;
    long nextz = (y + mid) * 100 / (x + mid);
    if (nextz > z) { // 승률이 변했을까?
      if (answer > mid) 
        answer = mid;
      top = mid - 1;
    } else {
      bottom = mid + 1;
    }
  }

  cout << answer << endl;
}