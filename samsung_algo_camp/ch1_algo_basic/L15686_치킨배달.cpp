#include <iostream>
#include <queue>
#include <string.h>
#include <vector>

using namespace std;

int n, m;
int city[50][50];
int chic_dist[50][50];
int m_selected[50][50];
bool visit[50][50];
typedef pair<int, int> pii;

int di[4] = {1, -1, 0, 0};
int dj[4] = {0, 0, 1, -1};

bool check_range(int i, int j) {
  if (0 <= i && i < n)
    if (0 <= j && j < n) 
      return true;
  
  return false;
}

void find_m_chic(int _i, int _j) {
  // dfs로 치킨집 m개 선택
  vector<pii> s;
  memset(visit, 0, sizeof(visit));
  int mcnt = 0;
  s.push_back(pii(_i, _j));
  while (!s.empty()) {
    pii cur = s.back();
    s.pop_back();
    int ci = cur.first;
    int cj = cur.second;

    if (city[ci][cj] == 2) {
      mcnt++;
      m_selected[ci][cj] = 1;
    }
    if (mcnt == m) return;

    for (int i = 0; i < 4; i++) {
      int adi = ci + di[i];
      int adj = cj + dj[i];
      if (check_range(adi, adj) && !visit[adi][adj]) {
        visit[adi][adj] = 1;
        s.push_back(pii(adi, adj));
      }
    }
  }
}

int get_chic_dist(int _i, int _j) {
  memset(visit, 0, sizeof(visit));

  queue<pii> q;
  int dist;
  int qsize;
  q.push(pii(_i, _j));

  for (dist = 0;!q.empty();dist++) {
    qsize = q.size();
    for (int i = 0; i < qsize; i++){
      pii cur = q.front();
      q.pop();

      int ci = cur.first;
      int cj = cur.second;

      if (m_selected[ci][cj] == 1) {
        return dist;
      }

      for (int k = 0; k < 4; k++) {
        int adi = ci + di[k];
        int adj = cj + dj[k];
        
        if (check_range(adi, adj) && !visit[adi][adj]) {
          visit[adi][adj] = 1;
          q.push(pii(adi, adj));
        }
      }
    }
  }
  return 0;
}

int get_chic_dist_sum() {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (city[i][j] == 1) {
        
      }
    }
}

int main() {
  // input
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      scanf("%d", &city[i][j]);
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (city[i][j] == 2) { // 치킨집
        memset(m_selected, 0, sizeof(m_selected));
        find_m_chic(i, j);


      }
    }
  }



}