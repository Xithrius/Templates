/*
Charles Buell
29 November 2018

Program purpose:
Get answers from student, make them answer again
if they didn't answer in one of the options,
and after the test is done they get which Questions
they got wrong, and how many incorrect and correct
they got
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
/*
My run is incorrect and I don't know what to fix in my program.
Please enter the student's answers for each of the questions.
Press Enter after typing each answer.
Please enter only an A, B, C, D or a, b, c, d for each question.
Question 1: A
Question 2: C
Question 3: B
Question 4: B
Question 5: a
Question 6: d
Question 7: d
Question 8: d
Question 9: a
Question 10: b
Question 11: v
Use only an A, B, C, D or a, b, c, d!
Please try again.
Question 11: a
Question 12: F
Use only an A, B, C, D or a, b, c, d!
Please try again.
Question 12: d
Question 13: a
Question 14: A
Question 15: C
Question 16: B
Question 17: A
Question 18: D
Question 19: B
Question 20: C
Questions that were answered incorrectly:
1
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
The student failed the exam
Correct answers: 2
Incorrect answers: 16
*/
