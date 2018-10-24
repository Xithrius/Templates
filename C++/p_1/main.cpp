// This program prints "You Pass" if a student's average is
// 60 or higher and prints "You Fail" otherwise

/**Exercise 1:
 Run the  program three times using 80, 55 and
 60 for the  average.
 What  happens when you  input  60 as the  average?
 > Modify  the  first if statement so that the  program will
 also  print  “You Pass” if the  average equals 60.


 Exercise 2:   Modify  the  program so that it uses
 an if/else statement rather than  two  if statements.

 Exercise 3:   Modify  the  program from Exercise 2 to
 allow the  following categories:
 Invalid data  (data above 100),
 ‘A’ category (90–100),
 ‘B’ category (80–89),
 “You Pass” category (60–79),
  “You Fail” category (0–59).
 What  will  happen to your  program if you  enter
 a negative value such  as -12?*/

#include <iostream>
using namespace std;

int main()
{
	float average;	// holds the grade average

	cout << "Input your average:" << endl;
	cin >> average;

    if (average > 100 || < 0)
        cout << "Invalid data" << endl;
    else if (average > 90 && average <= 100)
        cout << "Category A" << endl;
    else if (80 < average < 89)
        cout << "Category B" << endl;
    else if (60 < average < 79)
        cout << "You pass" << endl;
    else
        cout << "You fail" << endl;


	return 0;
}
