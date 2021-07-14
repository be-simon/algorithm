#include <iostream>

using namespace std;

int n;

int main() {
  int answer = 0;
  cin >> n;
  long f1 = 0, f2 = 1, f3 = 0;

  if (n == 0)
    cout << f1 << endl;
  else if (n == 1) 
    cout << f2 << endl;
  else {
    for (int i = 0; i < n - 1; i++) {
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
    }
    cout << f3 << endl;
  }
}