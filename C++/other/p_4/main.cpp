#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Input first name: ";
    string name;
    cin >> name;
    cout << "Input seconds: ";
    int seconds;
    cin >> seconds;

    double minutes = seconds / 60;
    double hours = minutes / 60;

    if (seconds < 60) {
        cout << "00:00:" << seconds << endl;
    }
    if (seconds > 59) {
        cout << "00:" << minutes << ":" << seconds << endl;
    }
    if (minutes > 59) {
        cout << hours << ":" << minutes << ":" << seconds << endl;
    }

    return 0;

}
