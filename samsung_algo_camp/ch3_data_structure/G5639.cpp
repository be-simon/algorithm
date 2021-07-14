#include <iostream>
#include <vector>

using namespace std;

vector<int> tree;

void pre_to_post(int s, int e) {
  if (s > e) return;
  
  int root = tree[s];
  if (s == e) {
    printf("%d\n", root);
    return;
  }

  int i;
  for (i = s + 1; i <= e; i++) {
    if (tree[i] > root)
      break;
  }

  pre_to_post(s + 1, i - 1);
  pre_to_post(i, e);
  printf("%d\n", root);
}

int main() {
  int num, cnt = 0;
  while (scanf("%d", &num) != -1) {
    tree.push_back(num);
    cnt++;
  }

  pre_to_post(0,cnt - 1);
}