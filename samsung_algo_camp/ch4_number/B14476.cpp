#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> num (1000000);
typedef pair<int, int> pii;
vector<pii> sub_gcd (1000000); // first : front, second : back

int gcd (int a, int b) {
  if (b == 0) return a;
  else return gcd(b, a % b);
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> num[i];
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j <= n; j++) {
      
    }
  }
  
}