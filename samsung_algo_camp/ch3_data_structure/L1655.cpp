#include <iostream>
#include <queue>
#include <vector>

using namespace std;

priority_queue<int> max_pq;
priority_queue<int, vector<int>, greater<int> > min_pq;
int n;

int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    int num;
    scanf("%d", &num);

    if (max_pq.size() == min_pq.size())
      max_pq.push(num); // 한군데를 기준으로 하면 된다. 어느 큐 맨 위에 값을 mid로 할 것인가?
    else  // 항상 max_pq가 더 많거나 같다.
      min_pq.push(num);
    
    if (!max_pq.empty() && !min_pq.empty()) {
      if (max_pq.top() > min_pq.top()) { // 순서에 맞지 않으면 swap
        int min_v = min_pq.top();
        int max_v = max_pq.top();
        min_pq.pop();
        max_pq.pop();
        max_pq.push(min_v);
        min_pq.push(max_v);
      }
    }

    printf("%d\n", max_pq.top());
  }

}
