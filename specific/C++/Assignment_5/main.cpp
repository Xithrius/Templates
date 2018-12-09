/*
Sorry this is so late, but it finally works
Charles Buell
29 November 2018

Program gets information of person and calculates
ideal body weight.
*/


#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    ifstream inputFile;
    inputFile.open("names-1.txt");
    // getting the file and assigning it to a variable
    string name, lname;
    int feet, inch, estWeight;
    // assigning variables
    if (inputFile) {
        while (inputFile >> name >> lname >> feet >> inch) {
            // if inputFile cannot assign values to variables, program wont run
            // at the same time the while loop is assigning values to variables
            if (feet >= 5) {
            // if feet is more than 5, than will move on to next statement
                if (inch >= 1) {
                  // if feet happens to be exactly 5, than this checks that
                  // the program won't run
                    estWeight = 110 + ((feet - 5) * 12 + inch) * 5;
                    // estWeight is the calculation of ideal body weight
                    cout << "The ideal body weight for " << name;
                    cout << " is " << estWeight << " pounds" << endl;
                }
            }
            else if (feet < 5) {
              // if feet is less than 5, then ideal body weight will not be calculated
                cout << "Cannot calculate ideal body weight for " << name << endl;
            }
        }
    }
    else
      cout << "File could not be found/opened" << endl;
      // error message for file not found / cannot be opened
    inputFile.close();
    // closing the file
    return 0;
}


/*
Run is different since I don't have codeblocks
and also I have a different terminal

The ideal body weight for Tom is 185 pounds
The ideal body weight for Eaton is 135 pounds
The ideal body weight for Cary is 165 pounds
Cannot calculate ideal body weight for Omar

*/
