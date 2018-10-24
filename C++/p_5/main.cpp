/**

 Relational Operators and the if Statement
 Compile and Run the following program. Then
 do the following exercises.
 ￼
 Exercise 1: Run the program several times using a different input each time.
 Does the program do what you expect? Is so, explain what it is doing.
 If not, locate the error and fix it.

 Exercise 2: Modify the program so that the user inputs both values to be tested
 for equality. Make sure you have a prompt for each input.
 Test the program with pairs of values that are the same and that are different.

 Exercise 3: Modify the revised Exercise 2 program by replacing the two if statements
 with a single if/else statement. Run the program again to test the results.
 */
#include <iostream>
using namespace std;

int main()
{
    int num1,	// num1 is not initialized
    num2 = 5;	// num2 has been initialized to 5

    cout << "Please enter an integer"  << endl;
    cin >> num1;

    cout << "num1 = " << num1 << " and num2 = " << num2 << endl;

    if (num1 = num2)
        cout << "Hey, that is a coincidence!" << endl;
        cout << "The values are the same" << endl;


    if (num1 != num2)
        cout << "The values are not the same" << endl;


return 0;
}
