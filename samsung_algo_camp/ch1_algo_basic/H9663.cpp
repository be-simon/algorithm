#include <iostream>

using namespace std;

int n;
int answer;
int board[15]; 
// 굳이 이차원 배열에 모두 체크할 필요 없이 
// 행마다 하나만 있을 수 있으니 그 위치만 저장하면 된다.

void queen(int line) {
  if (line == n) {
    answer++;
    return;
  }

  for (int i = 0; i < n; i++) { // 해당 라인에서 가능한 곳 탐색
    bool isok = true;
    for (int j = 0; j < line; j++) { // 이전의 퀸들을 참조
      if (board[j] == i || abs(line-j) == abs(board[j] - i)) { 
        // 세로 or 대각으로 겹침
        // 대각은 이전의 퀸들과의 가로, 세로 거리가 같을 때 겹친다고 판단
        isok = false;
        break;
      }
    } 
    if (isok) {
      board[line] = i;
      queen(line + 1);
    }
  }
} 

int main() {
  cin >> n;
  queen(0);
  cout << answer << endl;
}