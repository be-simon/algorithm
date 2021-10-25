#include <iostream>

using namespace std;

int n, answer;
int tri[500][500];

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
      cin >> tri[i][j];
      if (i > 0) {
        if (j == 0)
          tri[i][j] += tri[i-1][j];
        else if(j == i) 
          tri[i][j] += tri[i-1][j-1];
        else 
          tri[i][j] += max(tri[i-1][j], tri[i-1][j-1]);
      }
      if (i == n-1 && answer < tri[i][j])
        answer = tri[i][j];
    }
  }
  
  cout << answer;
}