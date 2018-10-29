#include <iostream>

using namespace std;

int main()
{
    bool check = true;
    while (check != false) {
        cout << "Enter a number: ";
        int num;
        cin >> num;
        if (num == 1) {
            check = false;
            cout << "Right number" << endl;

        }

        else
            cout << "Wrong number" << endl;
            check = true;
    }
    return 0;
}
