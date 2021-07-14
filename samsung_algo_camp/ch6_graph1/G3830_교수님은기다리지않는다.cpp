#include <iostream>
#include <string.h>

using namespace std;

typedef long long ll;
int n, m;
int parent[100001];
ll d_to_p[100001];

void init(int n) {
  for (int i = 1; i <= n; i++) {
    parent[i] = i;
    d_to_p[i] = 0;
  }
}

int find_set(int a) {
  if (parent[a] == a) return a;
  else {
    int p = find_set(parent[a]);
    d_to_p[a] += d_to_p[parent[a]];
    return parent[a] = p;
  }
}

void union_set(int a, int b, ll weight) {
  int pa = find_set(a);
  int pb = find_set(b);
  
  if (pa != pb) {
    d_to_p[pa] = d_to_p[b] + weight - d_to_p[a];
    parent[pa] = pb;
  }
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  int a, b;
  ll w;
  char c;
  while(true) {
    cin >> n >> m;
    if (n == 0 && m == 0) return 0;

    init(n);
    
    for (int i = 0; i < m; i++) {
      cin >> c >> a >> b;
      if (c == '!') {
        cin >> w;
        union_set(a, b, w);
      } else if(c == '?') {
        if (find_set(a) != find_set(b))
          cout << "UNKNOWN\n";
        else {
          cout << d_to_p[a] - d_to_p[b] << "\n";
        }
      }
    }
  }

  return 0;
}