// Wednesday, November 14 2018
#include <iostream>
using namespace std;

void doSomething(int &a) {
  a += 1;
}

int main()
{
    int value = 5;

    cout << "value = " << value << '\n';
    doSomething(value);
    cout << "value = " << value << '\n';
    return 0;
}

// value = 5
// value = 6
