#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool prime_filter[3200];
vector<int> prime;

int main() {
  int n;
  cin >> n;
  if (n == 1) return 0;

  int r = round(sqrt(n));
  for (int i = 2; i <= r; i++) {
    if (prime_filter[i] == true) continue;
    for (int j = i * 2; j <= r; j += i) {
      prime_filter[j] = true;
    }
  }
  
  for (int i = 2; i <= r; i++) {
    if (prime_filter[i] == false) {
      prime.push_back(i);
    }
  }

  int size = prime.size();
  for (int i = 0; i < size; i++) {
    while (n % prime[i] == 0) {
      cout << prime[i] << endl;
      n /= prime[i];
    }
  }
  if (n > 1) { // n 자체가 큰 소수일 수도 있음
    cout << n << endl;
  }

}