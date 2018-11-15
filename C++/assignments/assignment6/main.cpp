#include <iostream>
#include <iomanip>
#include <algorithm>
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
    int middleHighest, middleLowest, i;
    double average;
    bool swapped = true;


    while (swapped) {
        swapped = false;
        for (i = 0; i < 3; ++i) {
            // if
            if (array[i + 1] < array[i]) {
                swap(array[i], array[i + 1]);
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
