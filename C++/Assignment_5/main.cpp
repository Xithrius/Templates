#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    ifstream inputFile;
    inputFile.open("names-1.txt");
    string name, lname;
    int feet, inch, estWeight;
    while (inputFile >> name  >> lname>> feet >> inch) {

        cout << name << endl;
        cout << feet << endl;
        cout << inch << endl;

        if (feet > 5) {
            estWeight = 110 + ((feet - 5) * 12 + inch) * 5;
            cout << "The ideal body weight for " << name;
            cout << " is " << estWeight << " pounds" << endl;
        }
        else
            cout << "Height < 5, nothing will be calculated" << endl;
        cout << "All calculations are complete" << endl;


    }
    inputFile.close();
    return 0;
}
