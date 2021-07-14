#include <iostream>
#include <vector>

using namespace std;

typedef pair<char, char> pcc;
vector<pcc> tree(91);
int n;

void preorder(char root) {
  if (root == '.') {
    return;
  }

  cout << root;
  preorder(tree[root].first);
  preorder(tree[root].second);
}

void inorder(char root) {
  if (root == '.') {
    return;
  }

  inorder(tree[root].first);
  cout << root;
  inorder(tree[root].second);
}

void postorder(char root) {
  if (root == '.') {
    return;
  }

  postorder(tree[root].first);
  postorder(tree[root].second);
  cout << root;
}


int main() {
  scanf("%d\n", &n);
  char r, l, c;
  for (int i = 0; i < n; i++) {
    scanf("%c %c %c", &r, &l, &c);
    getchar();
    tree[r] = pcc(l, c);
  }

  preorder('A');
  cout << endl;
  inorder('A');
  cout << endl;
  postorder('A');
  cout << endl;
}