/*
Charles Buell
11/14/2018
My program takes 4 judge scores, then takes
the middle two scores and averages them.

*/

#include <iostream>
#include <iomanip>

using namespace std;


void getJudgeData (int &a) {
    while (a > 20 || a < 0) {
        cout << a << " is an invalid score. Must be between 0 and 20" << endl;
        cout << "It must be a number between 0 to 20"<< endl;
        cout << "Enter the judge's score:" << endl;
        cin >> a;
    }
}

void calcScore(int array[4]) {

    // searching for the highest of the two middle scores
    int middleHighest, middleLowest, i, tmp;
    double average;
    bool swapped = true;


    while (swapped) {
        swapped = false;
        for (i = 0; i < 3; ++i) {
            // if the component behind another one is smaller,
            // the two switch places.
            if (array[i + 1] < array[i]) {
                tmp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = tmp;
                swapped = true;
            }
        }

    }

    middleHighest = array[2];
    middleLowest = array[1];
    average = (middleHighest + middleLowest) / 2;
    cout << "The performer's final score is ";
    cout << fixed << setprecision(1) << average;

}

int main() {

    int array[4];

    for (int i = 0; i < 4; i++) {
      cout << "Enter the judge's score: ";
      cin >> array[i];
      getJudgeData(array[i]);
    }

    calcScore(array);

    return 0;
}
/*
Enter the judge's score: 6
Enter the judge's score: 70
70 is an invalid score. Must be between 0 and 20
It must be a number between 0 to 20
Enter the judge's score:
19
Enter the judge's score: 10
Enter the judge's score: 8
The performer's final score is 9.0
Process returned 0 (0x0)   execution time : 11.604 s
Press any key to continue.



