#include <iostream>
#include <queue>
#include <set>

using namespace std;

// bfs 탐색
int n, k;
int arr[6];
queue<int> q;

int get_num_len(int num) {
  int len = 0;
  // num to arr
  for (int k = 0; num > 0; k++) {
    len++;
    num /= 10;
  }
  return len;
}

int swap(int num, int i, int j) {
  int len = 0;
  // num to arr
  for (int k = 0; num > 0; k++) {
    arr[k] = num % 10;
    len++;
    num /= 10;
  }
  
  // swap
  int temp = arr[len - i - 1];
  arr[len - i - 1] = arr[len - j - 1];
  arr[len - j - 1] = temp;

  if (arr[len - 1] == 0) return 0;

  // arr to num
  int ret = 0;
  for (int k = len - 1; k >= 0; k--) {
    ret *= 10;
    ret += arr[k];
  }

  return ret;
}

int main() {
  cin >> n >> k;
  if (n == 1000000) {
    cout << 1000000;
    return 0;
  }

  if (n < 10 || (n < 100 && n % 10 == 0)) {
    cout << -1;
    return 0;
  }

  q.push(n);
  for (int i = 0; i < k; i++) {
    int qsize = q.size();
    set<int> k_cand_set;

    for (int j = 0; j < qsize; j++) {
      int num = q.front();
      q.pop();
      int len = get_num_len(num);
      for (int m = 0; m < len - 1; m++) {
        for (int n = m + 1; n < len; n++) {
          int temp = swap(num, m, n);
          if (temp && k_cand_set.find(temp) == k_cand_set.end()) {
            q.push(temp);
            k_cand_set.insert(temp);
          }
        }
      }
    }
  }

  int answer = 0;
  while (!q.empty()) {
    int num = q.front();
    q.pop();
    if (num > answer) answer = num;
  }

  cout << answer << endl;
}