#include <iostream>

using namespace std;

int main() {
    int students, score;
    int i = 0;
    cout << "How many students? ";
    cin >> students;
    int scores[students * 3];
    cout << "Enter scores: " << endl;
    while (i <= students * 3) {
        cin >> score[i];
    }
    return 0;
}
