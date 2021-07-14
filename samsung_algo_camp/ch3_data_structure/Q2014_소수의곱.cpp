#include <iostream>
#include <queue>

using namespace std;

int k, n;
int arr[100];
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
  scanf("%d %d", &k, &n);
  for (int i = 0; i < k; i++) {
    scanf("%d", arr + i);
  }

  for (int i = 0; i < k; i++) {
    for (int j = i; j < k; j++) {
      if (i == j) {
        pq.push(arr[i]);
        pq.push(arr[i] * arr[i]);
      } else {
        pq.push(arr[i] * arr[j]);
      }

      cout << "i : " << i << ", j : " << j << " - " << arr[i] * arr[j] << endl;
    }
  }

  for (int i = 0; i < n - 1; i++) {
    cout << pq.top() << endl;
    pq.pop();
  }
  printf("%d\n", pq.top());
}