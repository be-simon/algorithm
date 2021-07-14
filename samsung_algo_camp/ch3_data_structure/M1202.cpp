#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int n, k;
long answer;
typedef pair<int, int> pii;
struct compare {
  bool operator()(pii a, pii b) {
    return a.second < b.second;
  }
};

vector<int> bags;
vector<pii> weight_min;
priority_queue<pii, vector<pii>, compare> value_max_pq;

int main() {
  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    int m, v;
    cin >> m >> v;
    weight_min.push_back(pii(m, v));
  }

  for (int i = 0; i < k; i++) {
    int b;
    cin >> b;
    bags.push_back(b);
  }

  sort(bags.begin(), bags.end());
  sort(weight_min.begin(), weight_min.end());

  int wi = 0;
  for (int i = 0; i < k; i++) {
    while (wi < n) {
      pii jewel = weight_min[wi];
      if (jewel.first <= bags[i]) {
        value_max_pq.push(jewel);
        wi++;
      } else break; 
    }

    if (!value_max_pq.empty()) {
      answer += value_max_pq.top().second;
      value_max_pq.pop();
    }
  }

  cout << answer << endl;
}