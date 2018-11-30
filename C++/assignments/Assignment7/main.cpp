/*
Your program should store the correct answers shown above in an array.
It should ask the user to enter the student’s answers for each of the 20 questions,
and the answers should be stored in another array.
After the student’s answers have been entered,
the program should display a message indicating whether the student passed or failed the exam.
(A student must correctly answer 15 of the 20 questions to pass the exam.)
It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions,
and a list showing the question numbers of the incorrectly answered questions.
Your program must have at least the following functions:

// Function prototype:

void input(char [], int);
void checkAnswers(char[], char[], int &, int &, int);
*. The input function accepts an array of characters and an integer for the size of the array.
   The function asks the user to input answers to the exam and stores them in the array.
   You must have an Input Validation loop:
   Only accept the letters A, B, C, D or a, b, c, d, as answers.

*. The checkAnswers function compares the values in the answers array
   to the values in the replies array.
   The number of correct and incorrect answers are stored in the correct
   and incorrect reference parameters.
*/

/*
Charles Buell
29 November 2018

Program purpose:
*/
#include <iostream>

using namespace std;

//void input(char [], int);
//void checkAnswers(char [], char [], int &, int &, int);

int main()
{
    int array_size = 20;
    char rightAnswers[array_size] = {'A', 'D', 'B', 'B', 'C',
                                     'B', 'A', 'B', 'C', 'D',
                                     'A', 'C', 'D', 'B', 'D',
                                     'C', 'C', 'A', 'D', 'B'};
    char userAnswers[array_size];
    cout << "Please enter the student's answers for each of the questions.";
    cout << endl;
    cout << "Press Enter after typing each answer." << endl;
    cout << "Please enter only an A, B, C, D or ";
    cout << "a, b, c, d for each question." << endl;
    int x;
    for (int i = 0; i == array_size; i++) {
        cin >> x;
        userAnswers[i] = x;
    }
    for (int i = 0; i == array_size; i++) {
      cout << userAnswers[i] << " ";
    }
    return 0;
}
/*
void input(char userAnswers[], int array_size)
{
    return 0;
}

void checkAnswers(char userAnswers[], char correctAnswers[], int &correct,
                  int &incorrect, int array_size)
{
    return 0;
}
*/
