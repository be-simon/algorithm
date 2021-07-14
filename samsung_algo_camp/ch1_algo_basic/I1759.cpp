#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int l, c;
vector<char> chs;
char answer[15];
bool isvowel[123];

void make_pw (int cur_pos, int start, int vowel_cnt) {
  if (cur_pos == l) { // 암호 하나를 만들었으면 출력
    if (vowel_cnt >= 1 && l - vowel_cnt >= 2){
      for (int i = 0; i < l; i++) 
        cout << answer[i];
      cout << endl;
      return;
    }
  }
  for (int i = start; i < c; i++) {
    answer[cur_pos] = chs[i];
    if (isvowel[answer[cur_pos]]) 
      make_pw(cur_pos + 1, i + 1, vowel_cnt + 1);  
    else
      make_pw(cur_pos + 1, i + 1, vowel_cnt);  

  }
}

int main() {
  cin >> l >> c ;
  for (int i = 0; i < c; i++) {
    char temp;
    cin >> temp;
    chs.push_back(temp);
  }

  isvowel['a'] = isvowel['e'] = isvowel['i'] = isvowel['o'] = isvowel['u'] = 1;

  sort(chs.begin(), chs.end());
  make_pw(0, 0, 0);
}