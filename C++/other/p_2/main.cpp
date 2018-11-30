#include <iostream>
#include <stdio.h>
#include <limits>

using namespace std;

int main()
{
    for ( int i = 0; i < 20; i += 1 ) {
        if ( i == 5) {
            cout << "Currently at 5" << endl;
        }
        if ( i == 10) {
            cout << "Currently at 10" << endl;
        } else {
            cout << "Value of i is " << i << endl;
        }
    }
}
