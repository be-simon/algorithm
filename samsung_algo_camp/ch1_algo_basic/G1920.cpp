#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;
int key;
vector<int> v(100000);

bool binary_search(int num) {
  int left, mid, right;

  left = 0;
  right = n - 1;
  while (left <= right) {
    mid = (left + right) / 2;

    if (v[mid] == num)
      return 1;
    else if (v[mid] < num) 
      left = mid + 1;
    else if (v[mid] > num) 
      right = mid - 1;
  }
  
  return 0;
}

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
  }
  sort(v.begin(), v.begin() + n);

  scanf("%d", &m);
  for (int i = 0; i < m; i++) {
    scanf("%d", &key);
    printf("%d\n", binary_search(key));
  }
}