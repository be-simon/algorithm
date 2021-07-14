#include <iostream>
#include <vector>

using namespace std;

int n, k, answer;
int alphabets[128];
vector<string> words;

bool check(int i) {
  int len = words[i].length();
  for (int j = 0; j < len; j++) {
    if (alphabets[words[i][j]] == 0) 
      return 0;
  }
  return 1;
}

void combination (char s, int c) {
  int cnt = 0;
  if (c == 0) {
    for (int i = 0; i < n; i++) {
      if (check(i))
        cnt++;
    }
    if (answer < cnt) answer = cnt;
  } else {
    for (int i = s; i <= 'z'; i++) {
      if (alphabets[i]) continue;
      else {
        alphabets[i] = 1;
        combination(i + 1, c - 1);
        alphabets[i] = 0;
      }
    }
  }
}

int main() {
  cin >> n >> k;

  char str[16];
  for (int i = 0; i < n ;i++) {
    scanf("%s", str);
    string s = str;
    words.push_back(s.substr(4, s.length() - 8));
  }

  if (k < 5) {
    printf("%d\n", 0);
    return 0;
  }
  if (k == 26) {
    printf("%d\n", n);
    return 0;
  }

  alphabets['a'] = 1;
  alphabets['c'] = 1;
  alphabets['i'] = 1;
  alphabets['n'] = 1;
  alphabets['t'] = 1;

  combination('b', k - 5);
  printf("%d\n", answer);
}