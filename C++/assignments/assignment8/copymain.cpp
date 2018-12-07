#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>

using namespace std;

void bubbleSort(int [], int);
int binarySearch(int [], int, int);
int mean(int []);

int main()
{
    ifstream inputFile;
    inputFile.open("nums-1.txt");
    if (!inputFile) {
        cout << "Unable to open/find file 'nums-1.txt'" << endl;
        inputFile.close();
    }
    int number, length = 0;
    bool check = true;
    while (check) {
        if (inputFile >> number) {
            length += 1;
        }
        else
            check = false;
    }
    int arr[length];
    for (int i = 0; i <= length - 1; i++) {
        inputFile >> arr[i];
        printf("%1d \n", arr[i]);
    }

    inputFile.close();
    return 0;
}
