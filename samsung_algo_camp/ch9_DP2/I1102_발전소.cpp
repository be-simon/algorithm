#include <iostream>
#include <string.h>

using namespace std;

int n, p;
int c[16][16];
char state[17]; // 거꾸로 줄꺼임
int dp[1<<16];

int power(int s, int cnt) { // s: 현재 state, cnt : 현재 켜져있는 발전소
  if (cnt == p)
    return 0;  
  
  if (dp[s] != -1) return dp[s]; // cost가 0일 때도 있기 때문에 -1로 해줘야함
  
  int ret = -1;

  for (int from = 0; from < n; from++) {
    if ((s & (1<<from)) == 0) // 켜져있는 발전소 체크
      continue; 

    for (int to = 0; to < n; to++) {
      if ((from == to) || (s & (1<<to))) // 꺼져있어야함
        continue;
      
      int v = power(s | (1<<to), cnt + 1) + c[from][to];
      ret = ret == -1 ? v : min(ret, v);
    }
  }

  dp[s] = ret;
  return ret;


  // for (int to = 0; to < n; to++) { // to 발전소를 켠다
  //   if ((s & (1 << to)) || (s == (s | (1 << to))))
  //     continue;
    
  //   int mc = -1; // min cost
  //   for (int from = 0; from < n; from++) { // 가동 중인거 찾아서 cost 비교
  //     if (from == to) continue;

  //     if (s & (1<<from)) // 가동 중인 발전소
  //       mc = mc == -1 ? c[from][to] : min(mc, c[from][to]);
  //   }

  //   int d = power(s | (1 << to), cnt + 1) + mc;
  //   if ((ret == -1) || (ret > d)) {
  //     ret = d;
  //   }
  // }
  // dp[s] = ret;
  // return dp[s];
}

int main() {
  memset(dp, -1, sizeof(dp));
  scanf("%d", &n);
  for (int i = 0; i < n; i++) 
    for (int j = 0; j < n; j++) 
      scanf("%d", &c[i][j]);
  scanf("%s %d", state, &p);

  int s = 0, cnt = 0 ;
  for (int i = 0; i < n; i++) {
    if (state[i] == 'Y') {
      s |= (1<<i);
      cnt++;
    }
  }

  if ((cnt == 0 && p == 0) || (cnt >= p)) { // 건드릴 필요 x
    printf("0\n");
    return 0;
  } else if (cnt == 0 && p > 0) { // 만족할 수 없음
    printf("-1\n");
    return 0;
  }
  
  printf("%d\n", power(s, cnt));
  
  return 0;
}
