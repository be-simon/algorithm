#include <iostream>

using namespace std;

int n, m, k;
int memo[101][101];
char answer[201];
int max_k = 1000000010;

int getAZ(int a, int z) { // a개와 z개를 가지고 만들 수 있는 문자열의 경우의 수
  if (a == 0 || z == 0)
    return 1;
  else if (memo[a][z] > 0)
    return memo[a][z];
  else {
    memo[a][z] = getAZ(a - 1, z) + getAZ(a, z - 1);
    if (memo[a][z] >= max_k) // k까지만 보면 되기 때문에 그 이상은 필요 없다.
      memo[a][z] = max_k;
    return memo[a][z];
  }
}

int main() {
  scanf("%d %d %d", &n, &m, &k);

  if (k > getAZ(n, m)){
    printf("%d\n", -1);
    return 0;
  }
  

  int acnt = n, zcnt = m;
  for (int i = 0; i < n + m; i++) {
    if (acnt > 0) { // a가 남아있으면
      int case_cnt = getAZ(acnt - 1, zcnt);
      if (k > case_cnt) { // a로 시작해도 k번째에 도달하지 않음
        answer[i] = 'z';
        k -= case_cnt;
        zcnt--;
      } else { // a로 시작하는 경우 안에 있음
        answer[i] = 'a';
        acnt--;
      }
    } else {
      answer[i] = 'z';
    }
  }
  answer[n + m] = '\0';
  printf("%s\n", answer);
}