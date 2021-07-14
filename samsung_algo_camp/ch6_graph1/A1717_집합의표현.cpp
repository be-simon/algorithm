#include <iostream>

// union find
// 합집합 = 같은 부모를 공유한다.
// union -> 같은 부모에 연결
// find -> 부모를 찾는다.

using namespace std;

int n, m;
int parent[1000001];

int _find(int a) { // 부모를 찾는다.
  if (a == parent[a]) return a;
  else  
    // return _find(parent[a]);
    // 이렇게 하면 시간이 오래 걸림
    // 매번 바로 위에 부모로만 가기 때문
    // 그냥 재귀로 조상을 찾은 후, 배열에 조상을 저장해두자.
    return parent[a] = _find(parent[a]);
}

void _union(int a, int b) { 
  // 한쪽에 붙인다.
  // 두 수의 부모를 찾고, 한쪽에 편승시킨다.
  int pa = _find(a);
  int pb = _find(b);
  parent[pa] = pb;
}

int main() {
  scanf("%d %d", &n, &m);

  for (int i = 1; i <= n; i++)
    parent[i] = i;

  int c, a, b;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &c, &a, &b);

    if (c == 1) {
      if (_find(a) == _find(b))
        printf("YES\n");
      else
        printf("NO\n");
    } else {
      _union(a, b);
    }
  }

  return 0;
}