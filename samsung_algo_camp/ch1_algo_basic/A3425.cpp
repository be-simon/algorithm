#include <iostream>
#include <stack>
#include <cstdlib>
#include <vector>

using namespace std;

stack<long> s;
vector<string> ops;

bool operate(string op) {
  if (s.empty()) {
    return false;
  } else { // 단항 연산
    if (op == "POP") {
      s.pop();
    } else if (op == "INV") {
      int temp = s.top();
      s.pop();
      s.push(-temp);
    } else if (op == "DUP") {
      s.push(s.top());
    } else if (s.size() <= 1){
      return false;
    } else { // 이항 연산
      long first = s.top();
      s.pop();
      long second = s.top();
      s.pop();
      if (op == "SWP") {
        s.push(first);
        s.push(second);
      } else if (op == "ADD") {
        s.push(first + second);
      } else if (op == "SUB") {
          s.push(second - first);
      } else if (op == "MUL") {
          s.push(first * second);
      } else if (first == 0) {
        return false;
      } else { // 나눗셈
        if (op == "DIV") {
          if ((first > 0 && second > 0) || (first < 0 && second < 0)) {
            s.push(abs(second) / abs(first));
          } else {
            s.push(-(abs(second) / abs(first)));
          }
        } else if (op == "MOD") {
          if (second > 0) {
            s.push(abs(second) % abs(first));
          } else {
            s.push(-(abs(second) % abs(first)));
          }
        }
      }
    }
  }

  return true;
}

int main() {
  string op;
  while (true) {
    ops.clear(); // initialize

    while (true) { // operator
      cin >> op;
      if (op == "QUIT")
        return 0;
      if (op == "END")
        break;
      ops.push_back(op);
    } 

    int n, first_num;
    bool result = true;
    cin >> n;

    for (int i = 0; i < n; i++) { // program
      while (!s.empty()) s.pop(); // stack init
      cin >> first_num;
      s.push(first_num);
      
      for (int j = 0; j < ops.size(); j++) { // operation ops
        op = ops[j];
        if (op == "NUM") {
          s.push(stol(ops[++j]));
        } else {
          result = operate(op);
          if(result == false)
            break;
        }
      }

      if (result == false || s.size() != 1 || abs(s.top()) > 1000000000) {
        cout << "ERROR" << endl;
      } else {
        cout << s.top() << endl;
      }
    }
    cout << endl;
  }
}