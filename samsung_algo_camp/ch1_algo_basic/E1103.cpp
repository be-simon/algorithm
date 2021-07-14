#include <iostream>

using namespace std;
typedef pair<int, int> pii;

int n, m, answer;
char board[50][51];
int visit[50][50];
int memo[50][50];

int di[] = {1, -1, 0, 0};
int dj[] = {0, 0, 1, -1};
bool isCycle = false;

bool check_range(int i, int j) {
  return (0 <= i && i < n && 0 <= j && j < m);
}

void dfs (int i, int j, int cnt) { // cnt는 현재까지 진행해 온 단계
  answer = max(answer, cnt);

  int num = board[i][j] - '0';
  for (int k = 0; k < 4; k++) {
    int adi = i + di[k] * num;
    int adj = j + dj[k] * num;

    // 이동 가능
    if (!check_range(adi, adj) || board[adi][adj] == 'H' || memo[adi][adj] > cnt + 1) // 이미 다른 경로에서 더 오래 있었음
      continue;
    else {
      if (visit[adi][adj] > 0) {
        isCycle = true;
        return;
      }
      
      visit[adi][adj] = 1;
      memo[i][j] = max(memo[adi][adj], cnt + 1);
      dfs(adi, adj, cnt + 1);  
      
      if (isCycle) return;
    }
  }
  visit[i][j] = 0;
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    scanf("%s", &board[i]);
  }

  visit[0][0] = 1;
  dfs(0, 0, 1);

  if (isCycle) 
    cout << -1 << endl;
  else
    cout << answer << endl;
  
  return 0;
}