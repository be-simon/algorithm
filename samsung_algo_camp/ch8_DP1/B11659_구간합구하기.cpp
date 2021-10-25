#include <iostream>

using namespace std;

int n, m;
int seg_sum[100001];

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  
  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    int a;
    cin >> a;
    seg_sum[i] = seg_sum[i-1] + a;
  }

  for (int i = 0; i < m; i++) {
    int s, e;
    cin >> s >> e;

    cout << seg_sum[e] - seg_sum[s-1] << "\n";
  }
}
