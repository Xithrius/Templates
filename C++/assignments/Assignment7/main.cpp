/*
Charles Buell
29 November 2018

Program purpose:
*/
#include <iostream>

using namespace std;

void input(char [], int);
void checkAnswers(char [], char [], int &, int &, int);

int main()
{
    int array_size = 20;
    int correct, incorrect;
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
    input(userAnswers, array_size);
    checkAnswers(userAnswers, rightAnswers, correct,
                 incorrect, array_size);
    if (correct <= 14) {
        cout << "The student failed the exam" << endl;
    }
    else if (correct >= 15) {
        cout << "The student passed the exam" << endl;
    }
    cout << "Correct answers: " << correct << endl;
    cout << "Incorrect answers: " << incorrect << endl;

    return 0;
}

void input(char userAnswers[], int z)
{
    int i = 0;
    while (i < z) {
        cout << "Question " << i + 1 << ": ";
        cin >> userAnswers[i];
        if (userAnswers[i] != 'A' &&
            userAnswers[i] != 'B' &&
            userAnswers[i] != 'C' &&
            userAnswers[i] != 'D' &&
            userAnswers[i] != 'a' &&
            userAnswers[i] != 'b' &&
            userAnswers[i] != 'c' &&
            userAnswers[i] != 'd') {
                cout << "Use only an A, B, C, D or a, b, c, d!" << endl;
                cout << "Please try again." << endl;
            }
        else
            i++;
    }
}

void checkAnswers(char userAnswers[], char rightAnswers[], int &correct,
                  int &incorrect, int array_size)
{
    correct = 0;
    incorrect = 0;
    int i = 0;
    cout << "Questions that were answered incorrectly: " << endl;
    while (i < array_size) {
        if (userAnswers[i] == rightAnswers[i]) {
            ++correct;
            ++i;
        }
        else
            ++incorrect;
            cout << i << endl;
            ++i;
    }
}
