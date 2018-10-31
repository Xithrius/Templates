/*

Charles Buell
ID: 20328941
10/30/2018, 8:18pm

This program asks you for what package you selected, then calculates the cost
of the one you selected, and the difference if you got a different package.
It will tell you if there's any difference, and also if there is none.

*/


#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    // PACKAGE A
    cout << "1. Package A: " << endl;
    cout << "   $39.99/month, 450 minutes are provided. " << endl;
    cout << "   Additional minutes are $0.45/min." << endl;
    const float aPackage = 39.99;
    // the base cost per month, $39.99
    const float aMinutes = 450.00;
    // how many minutes limited per month, 450 minutes
    const float aRate = 0.45;
    // if the limit of minutes is exceeded, $0.45 will be charged every minute

    // PACKAGE B
    cout << "2. Package B: " << endl;
    cout << "   $59.99/moth, 900 minutes are provided. " << endl;
    cout << "   Additional minutes are $0.40/min." << endl;
    const float bPackage = 59.99;
    // the base cost per month, $59.99
    const float bMinutes = 900.00;
    // how many minutes limited per month, 900 minutes
    const float bRate = 0.40;
    // if the limit of minutes is exceeded, $0.40 will be charged every minute

    // PACKAGE C
    cout << "3. Package C: " << endl;
    cout << "   $69.99/month, unlimited minutes provided." << endl;
    const float cPackage = 69.99;
    // the base cost per month, $69.99


    cout << "Select a subscription package [1/2/3/4]: ";
    // Choosing a subscription package, and then applying it to an integer
    int packageChoice;
    cin >> packageChoice;
    const int packageA = 1;
    const int packageB = 2;
    const int packageC = 3;

    cout << "Integer minutes used: ";
    int minutes;
    cin >> minutes;
    // how many minutes the user used, then assigning it to a variable


    float aCost, bCost, cCost, saved;
    // initializing the costs of all packages, and how much would be saved.
    if (minutes > aMinutes)
        aCost = aPackage + ((minutes - aMinutes) * aRate);
    // if minutes that are used is greater than the package,
    // additional rates by aRate will be used, and apply it to aCost
    else
        aCost = aPackage;
    // if minutes are not exceeded, then cost will be base rate, or the package.

    if (minutes > bMinutes)
        bCost = bPackage + ((minutes - bMinutes) * bRate);
    // if minutes that are used is greater than the package,
    // additional rates by aRate will be used, and apply it to bCost
    else
        bCost = bPackage;
    cCost = cPackage;
    // the C package has unlimited minutes,
    // so there will be no extra charge no matter what



    switch(packageChoice) {


    // if package A was selected
    case(packageA):
        cout << "package A selected" << endl;
        cout << "Cost: $" << aCost << endl;
        if (aCost > bCost) {
            saved = aCost - bCost;
            cout << "If B package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package B vs A, it will be told here.
        }
        else
            cout << "No savings: Package B" << endl;
        if (aCost > cCost) {
            saved = aCost - cCost;
            cout << "If C package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package C vs A, it will be told here.
        }
        else
            cout << "No savings: Package C" << endl;

        break;


    // if package B was selected
    case(packageB):
        cout << "package B selected" << endl;
        cout << "Cost: $" << bCost << endl;
        if (bCost > aCost) {
            saved = bCost - aCost;
            cout << "If A package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package B vs A, it will be told here.
        }
        else
            cout << "No savings: Package A" << endl;
        if (bCost > cCost) {
            saved = bCost - cCost;
            cout << "If C package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package B vs C, it will be told here.
        }
        else
            cout << "No savings: Package C" << endl;
        break;


    // if package C was selected
    case(packageC):
        cout << "package C selected" << endl;
        cout << "Cost: $" << cCost << endl;
        if (cCost > aCost) {
            saved = cCost - aCost;
            cout << "If A package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package C vs A, it will be told here.
        }
        else
            cout << "No savings: Package A" << endl;
        if (cCost > bCost) {
            saved = cCost - bCost;
            cout << "If B package was selected, $" << saved;
            cout << " Would've been saved" << endl;
        // if you could've saved with package C vs B, it will be told here.
        }
        else
            cout << "No savings: Package B" << endl;
        break;

    default:
        cout << "Please Choose a package that is either ";
        cout << "1, 2, 3, or 4. Restart the program to try again." << endl;
        break;
    // if none of the packages where selected, the user will be rerouted here.

    }

    return 0;
}

/*
sample Run:

1. Package A:
   $39.99/month, 450 minutes are provided.
   Additional minutes are $0.45/min.
2. Package B:
   $59.99/moth, 900 minutes are provided.
   Additional minutes are $0.40/min.
3. Package C:
   $69.99/month, unlimited minutes provided.
Select a subscription package [1/2/3/4]: 2
Integer minutes used: 350
package B selected
Cost: $59.99
If A package was selected, $20 Would've been saved
No savings: Package C
*/
