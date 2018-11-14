#include <iostream>
using namespace std;

void dashedLine(int a) {
    if (a > 0) {
        while (a > 0) {
            cout << "-";
            --a;
        }
    }
}

int main() {
  dashedLine(2);
}
