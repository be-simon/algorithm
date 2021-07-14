#include <iostream>

using namespace std;

int  n, m;
int seq[10000];

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    scanf("%d", seq+i);
  }

  int sum = 0;
  int answer = 0;
  int l = 0, r = 0;
  for (;r < n; r++) {
    sum += seq[r];
    while (sum > m) {
      sum -= seq[l];
      l++;
    }
    if (sum == m) 
      answer++;
  }

  cout << answer << endl;
}