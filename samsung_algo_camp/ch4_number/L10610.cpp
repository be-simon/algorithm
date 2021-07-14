#include <iostream>

using namespace std;

char num[100001];
int sum;
int digit_cnt[128];

int main() {
  scanf("%s", num);
  for (int i = 0; num[i]; i++) {
    sum += num[i] - '0';
    digit_cnt[num[i]]++;
  }
  if (digit_cnt['0'] == 0 || sum % 3 != 0) {
    cout << -1 << endl;
    return 0;
  }

  // sort를 해도 되지만 숫자 개수를 카운트하는 방법
  for (int i = '9'; i >= '0'; i--) {
    for (int j = 0; j < digit_cnt[i]; j++) {
      printf("%c", i);
    }
  }
}