#include <iostream>

using namespace std;

int n, h;
int answer, cnt;
int obs_cnt[500001];

int main() {
  cin >> n >> h;
  int obs;
  for (int i = 0; i < n; i++) { // +1, -1 누적합을 이용
    cin >> obs;
    if (i % 2 == 0) { // 석순
      obs_cnt[0]++;
      obs_cnt[obs]--;
    } else { // 종유석
      obs_cnt[h - obs]++;
    }
  }

  int sum = 0;
  answer = -1;
  for (int i = 0; i < h; i++) {
    sum += obs_cnt[i];
    if (answer == -1 || sum < answer) {
      answer = sum;
      cnt = 1;
    }
    else if (sum == answer)
      cnt++;
  }

  cout << answer << " " << cnt << endl;
}