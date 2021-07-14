#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int n;
int in[501];
vector<int> g[501];
int btime[501];
int time_cache[501];

int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    int t, prev;
    scanf("%d", &t);
    btime[i] = t;
  
    scanf("%d", &prev);
    while(prev != -1) {
      g[prev].push_back(i);
      in[i]++;
      scanf("%d", &prev);
    }
  }

  queue<int> q;
  for (int i = 1; i <= n; i++) 
    if (in[i] == 0) {
      q.push(i);
      time_cache[i] = btime[i];
    }

  while(!q.empty()) {
    int cur = q.front(); q.pop();
    btime[cur] = time_cache[cur];

    for (int next : g[cur]) {
      in[next]--;
      int t_sum = btime[next] + btime[cur];
      time_cache[next] = max(time_cache[next], t_sum);
      
      if (in[next] == 0)
        q.push(next);
    }
  }

  for (int i = 1; i <= n; i++) {
    printf("%d\n", btime[i]);
  }
}