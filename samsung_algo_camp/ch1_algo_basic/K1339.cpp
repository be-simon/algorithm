#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// 숫자의 특성을 이용해보자
  // ABC = 100*A + 10*B + C 

typedef pair<char, int> pci;
int n;
vector<string> words;
map<char, int> chs;

bool compare(pci& a, pci& b) { // value 기준 정렬
  if (a.second == b.second) 
    return 0;
  else 
    return a.second > b.second;
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    string temp;
    cin >> temp;
    words.push_back(temp);
  }

  for (string s : words) {
    int len = s.length();
    int pos = 1;
    map<char, int>::iterator itr;
    for (int i = len - 1; i >= 0; i--) {
      itr = chs.find(s[i]);
      if (itr == chs.end()) { // 맵에 없음
        chs[s[i]] = pos;
      } else {
        itr->second += pos;
      }
      pos *= 10;
    }
  }


  // 자리수 기준으로 sorting
  vector<pci> v (chs.begin(), chs.end());
  sort(v.begin(), v.end(), compare);

  vector<pci>::iterator itr;
  int factor;
  int sum = 0;
  for (factor = 9, itr = v.begin(); itr != v.end(); itr++, factor--) {
    sum += itr->second * factor;
  }

  cout << sum << endl;

}