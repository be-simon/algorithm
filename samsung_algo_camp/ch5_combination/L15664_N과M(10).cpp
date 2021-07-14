#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int arr[8];
int answer[8];
bool used[8];

void make_seq(int k) {
  if (k == m) { // 문자열 생성 완료
    for (int i = 0; i < m; i++)
      printf("%d ", answer[i]);
    printf("\n");
    return;
  } else {
    int prev = 0;
    for (int i = 0; i < n; i++) {
      if (used[i]) continue;
      if (prev == arr[i]) continue;
      if (k > 0 && answer[k-1] > arr[i]) continue;
      
      used[i] = true;
      answer[k] = arr[i];
      prev = arr[i];
      make_seq(k + 1);
      used[i] = false;
    }
  }

}

int main() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%d", arr + i);
  }
  sort(arr, arr + n);

  make_seq(0);
}