/*The Speed of Sound

This table shows the approximate speed of sound in air,water,and steel.

Medium                  Speed

Air                   1,100 feet per second
Water                 4,900 feet per second
Steel                 16,400 feet per second

Write a program that displays a menu allowing the user to select air,
water, or steel. After the user has made a selection, he or she should
be asked to enter the distance a sound wave will travel in the selected
medium. The program will then display the amount of time it will take.
(Round the answer to four decimal places.) time =  distance / speed ;

Input Validation: Check that the user has selected one of the available
choices from the menu. Do not accept distances less than 0.
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	// Constants for speeds
	const double AIR   = 1100,
                 WATER = 4900,
                 STEEL = 16400;

	// Constants for menu choices
	const int AIR_CHOICE   = 1,
              WATER_CHOICE = 2,
              STEEL_CHOICE = 3;

	int choice; 		// To hold a menu choice
	double distance, speed, time;

	// Display the menu and get a choice.
	cout << "Select a medium:\n"
		 << "1. Air\n"
		 << "2. Water\n"
		 << "3. Steel\n\n"
		 << "Enter your choice: ";
	cin  >> choice;

	// Set the numeric output formatting.
	cout << fixed << setprecision(4);

	// Respond to the user's menu selection.
	switch(choice)
	{
        case(AIR_CHOICE):
            // Validate the distance.
			if (distance > 0)
			{

			}
			else

			break;

		case():



			// Validate the distance.
			if (distance > 0)
			{

			}
			else

			break;

		case(''):



			// Validate the distance.
			if (distance > 0)
			{


			}
			else

			break;

		default:
			cout << "\nThe valid choices are 1 through 3. Run the\n"
				 << "program again and select one of those.\n";
	}

	return 0;
}
