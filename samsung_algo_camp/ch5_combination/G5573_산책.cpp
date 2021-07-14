#include <iostream>

using namespace std;

int h, w, n;
int road[1001][1001];
int visit_cnt[1001][1001];

int main() {
  scanf("%d %d %d", &h, &w, &n);
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      scanf("%d", &road[i][j]);
    }
  }

  visit_cnt[0][0] = n - 1;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      // if (i == 0 || j == 0) continue;
      
      if (visit_cnt[i][j] == 0) continue;
      if (visit_cnt[i][j] % 2 == 0) { // 짝수번 방문
        visit_cnt[i + 1][j] += visit_cnt[i][j] / 2;
        visit_cnt[i][j + 1] += visit_cnt[i][j] / 2;
      } else { // 홀수번 방문
        if (road[i][j] == 0) { // 아래쪽
          road[i][j] = 1;
          visit_cnt[i + 1][j] += visit_cnt[i][j] / 2 + 1;
          visit_cnt[i][j + 1] += visit_cnt[i][j] / 2;
        } else if (road[i][j] == 1) { // 오른쪽
          road[i][j] = 0;
          visit_cnt[i][j + 1] += visit_cnt[i][j] / 2 + 1;
          visit_cnt[i + 1][j] += visit_cnt[i][j] / 2;
        }
      }
    }
  }

  int i = 0, j = 0;
  while (i < h && j < w) {
    if (road[i][j] == 0)
      i++;
    else j++;
  }

  printf("%d %d\n", i + 1, j + 1);
}