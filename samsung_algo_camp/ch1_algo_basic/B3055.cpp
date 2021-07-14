#include <iostream>
#include <queue>
#include <vector>
using namespace std;

typedef pair<int, int> pii; // 좌표

int r, c;
char forest[50][51]; // \n 고려
int answer;

int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
bool check_range(int _r, int _c) {
  return 0 <= _r && _r < r && 0 <= _c && _c < c;
}

// 물 따로 두더지 따로 이동
// 매 턴마다 이동하는 식으로 구현해볼까?

queue<pii>ddg_q, water_q;
int ddg_visit[50][50] = {0, }, water_visit[50][50] = {0, };

int main() {
  cin >> r >> c;
  for (int i = 0; i < r; i++) {
    scanf("%s", forest[i]);
  }

  for (int i = 0 ; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if (forest[i][j] == 'S') {
        ddg_q.push(pii(i, j));
        ddg_visit[i][j] = 1;
      } else if (forest[i][j] == '*') {
        water_q.push(pii(i, j));
        water_visit[i][j] = 1;
      }
    }
  }

  answer = 0;
  while (!ddg_q.empty()) {
    answer++;
    int qsize;

    qsize = water_q.size();
    for (int i = 0; i < qsize; i++) { // 물 이동
      pii cur_water = water_q.front();
      water_q.pop();
      
      for (int j = 0; j < 4; j++) {
        int adr, adc;
        adr = cur_water.first + dr[j];
        adc = cur_water.second + dc[j];
        
        // 이동 불가
        if (!check_range(adr, adc)) 
          continue;
        if (forest[adr][adc] == 'D' || forest[adr][adc] == 'X' || water_visit[adr][adc] > 0) 
          continue;

        water_visit[adr][adc] = 1;
        water_q.push(pii(adr, adc));
      }
    }

    qsize = ddg_q.size();
    for (int i = 0; i < qsize; i++) {
      pii cur_ddg = ddg_q.front();
      ddg_q.pop();

      for (int j = 0; j < 4; j++) {
        int adr, adc;
        adr = cur_ddg.first + dr[j];
        adc = cur_ddg.second + dc[j];
        
        if (forest[adr][adc] == 'D') { // find answer
          cout << answer << endl;
          return 0;
        }

        // 이동 불가
        if (!check_range(adr, adc)) 
          continue;
        if (forest[adr][adc] == 'X' || ddg_visit[adr][adc] > 0 || water_visit[adr][adc] > 0) 
          continue;
        
        ddg_visit[adr][adc] = 1;
        ddg_q.push(pii(adr, adc));
      }      
    }
  }

  cout << "KAKTUS" << endl;
  return 0;
}



