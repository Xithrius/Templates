#include <iostream>
#include <string>

using namespace std;

int main() {
    string statement;
    char char1;
    cout << "Enter a statement: ";
    getline(cin, statement);
    cout << "Enter a character: ";
    cin >> char1;
    int i = 0, timesSeen = 0;
    while (statement[i] != '\0') {
        if (statement[i] == char1)
          timesSeen++;
        i++;
    }
    cout << char1 << " was seen " << timesSeen << " times" << endl;
    return 0;
}
