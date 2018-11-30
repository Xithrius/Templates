#include <iostream>
#include <iomanip>
#include <ctype.h>

using namespace std;

void input(char[], int);
void checkAnswers(char[], char[], int &, int &, int);



int main()
{
   char questions[20];
   const int Total = 20;
   char rightAnswers[] = {'A', 'D', 'B', 'B', 'C',
                          'B', 'A', 'B', 'C', 'D',
                          'A', 'C', 'D', 'B', 'D',
                          'C', 'C', 'A', 'D','B'};

   cout << "Please enter the student's answers " << endl;
   cout << "Press Enter after typing each answer." << endl;
   cout << "Please enter a valid choice" << endl;
   cout << "A, B, C, D or a, b, c, d" << endl;

    input(ques, arrTotal);
    checkAnswers(ques, rightAns, correct, incorrect, arrTotal);

    if ( correct <= 12)
    {
        cout << "The student has failed" << endl;
    }
    else
    {
        cout << "The student has passed" << endl;
    }

    cout << "Correct Answers: " << correct << endl;
    cout << "Incorrect Answers: " << incorrect << endl;

 }

 void input (char question[], int arrT)
 {

     for ( int i = 1; i <= 20; i++ )
     {
         cout << "Question " << i << ": " << endl;
         cin >> question[i];

         while (question[i] != 'A' &&
                question[i] != 'B' &&
                question[i] != 'C' &&
                question[i] != 'D' &&
                question[i] != 'a' &&
                question[i] != 'b' &&
                question[i] != 'c' &&
                question[i] != 'd')
     {

         cout << "Use only an A, B, C, D or a, b, c, d!" << endl;
         cout << "Please try again." << endl;
         cin >> question[i];

     }
         putchar(toupper(question[i]));
     }


}

void checkAnswers(char question[], char answer[], int &right, int &wrong, int arrT)
{
    int counter;
    cout << "Question that were answered incorrectly:" << endl;

   for ( int i = 0; i < arrT; i++)
   {
    if (question[i] == answer[i])
    {
        right++;
    }
    else
    {
        wrong++;
        counter = i +1;
        cout << counter << endl;
    }
   }


}
