#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    // PACKAGE A
    cout << "1. Package A: " << endl;
    cout << setw(2) << "$39.99/month, 450 minutes are provided. " << endl;
    cout << setw(2) << "Additional minutes are $0.45/min." << endl;
    const float aRate = 39.99;
    const int aMinutes = 450;
    const float aAdditional = 0.45;

    // PACKAGE B
    cout << "Package B: ";
    cout << "$59.99/moth, 900 minutes are provided. ";
    cout << "Additional minutes are $0.40/min." << endl;
    const float bRate = 59.99;
    const int bMinutes = 900;
    const float bAdditional = 0.40;

    // PACKAGE C
    cout << "Package C: ";
    cout << "$69.99/month, unlimited minutes provided." << endl;
    const float cRate = 69.99;


    cout << "Select a subscription package: ";
    char packageChoice;
    cin >> packageChoice;

    switch(packageChoice) {
    case 'A':

    case 'B':

    case 'C':

    case 'quit':
        //

    default:
        //

    }

    return 0;
}
