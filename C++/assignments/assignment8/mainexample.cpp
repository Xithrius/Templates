#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int binarySearch(int [], int, int );
void bubbleSort(int [], int);
void printArray(int [], int);
int mean( int []);
int main()
{
    int arr[12];
    int value;
    int sum;
    int average;


    ifstream inFile;
    inFile.open("nums-1.txt");

    if (!inFile)
    {
        cout << "Unable to open file" << endl;
    }

    for (int i = 0; i < 12; i++)
    {
        inFile >> arr[i];
    }

    cout << "Enter an integer to search for: " << endl;
    cin >> value;

    cout << "The array entered by the user is as follows: " << endl;
    printArray(arr, 12);

    cout << "The item searched for is " << value << endl;
    cout << "The value " << value << " is in the postion number ";
    cout << binarySearch(arr, 12, value) << " of the list." << endl;

    for (int i = 0; i < 12; i++)
    {
       sum += arr[i];
    }
    average = sum / 12;
    cout << "The mean of all the elements in the array is ";
    cout << fixed << setprecision(1) << average << endl;

}

int binarySearch(int arr[], int sizeArr, int value)
{
    int first = 0;
    int last = sizeArr - 1;
    int middle;
    int position = -1;
    bool found = false;


    while (!found && first <= last)
    {
        middle = (first + last ) / 2;
        if (arr[middle] == value)
        {
            found = true;
            position = middle;
        }
        else if (arr[middle] > value)
            last = middle - 1;
        else first = middle + 1;
    }

    return position;
}

void bubbleSort(int arr[], int n)
{
   bool swap;
   int temp;

   do
   {
       swap == false;

       for ( int i = 0; i < n - 1; i ++)
       {
           temp = arr[i];
           arr[i] = arr[i + 1];
           arr[i + 1] = temp;
           swap = true;
       }
   }
   while(swap);
}



void printArray(int arr[], int sizeArr)
{
    int i;
    for (i=0; i < sizeArr; i++)
        printf(" ", arr[i]);
    printf("n");
}
