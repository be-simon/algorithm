#include <iostream>
#include <map>

using namespace std;

int n, m;

map<int, int> year_rain;
int tree[1 << 17];

int get_max(int node, int s, int e, int l, int r) {
  if (r < s || e < l) 
    return 0;
  else if (l <= s && e <= r) 
    
  else {
    

  }
}

void update(int node, int s, int e, int i, int v) {

}


int main() {
  scanf("%d", &n);
  int y, r;
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &y, &r);
    year_rain.insert(make_pair(y, r));
  }
  scanf("%d", &m);
  int y, x;
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &y, &x);
  }
}