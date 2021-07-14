#include <iostream>

using namespace std;

int gcd (int a, int b) {
  if (b == 0) return a;
  else 
    return gcd(b, a % b);
}

int main() {
  int a, b, c, d, p, q;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  p = a * d + b * c;
  q = b * d;
  
  int g = gcd(p, q);
  cout << p / g << " " << q / g << endl;
}