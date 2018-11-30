#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    ifstream inputFile;
    inputFile.open("names-1.txt");
    string name;
    int feet, inch, estWeight;
    bool check = true;
    while (check) {
        inputFile >> name;
        inputFile >> feet;
        inputFile >> inch;
        cout << name << feet << inch << endl;

        if (feet > 5) {
            estWeight = 110 + ((feet - 5) * 12 + inch) * 5;
            cout << "The ideal body weight for " << name;
            cout << " is " << estWeight << " pounds" << endl;
        }
        else
            cout << "Height < 5, nothing will be calculated" << endl;
        cout << "All calculations are complete" << endl;
        inputFile.close();
        if (!(inputFile >> name) || !(inputFile >> feet) || !(inputFile >> inch))
            check = false;
    }

    return 0;
}
