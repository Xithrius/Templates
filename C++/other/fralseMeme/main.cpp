#include <iostream>

using namespace std;

int main()
{
    bool condition = true;
    if (condition != false &&
        condition == true &&
        condition == !!true &&
        !condition == false &&
        !condition == !true &&


        !!condition == true &&
        !!!condition == !true &&
        !!!!condition == !!true &&
        !!!!!condition == !!!true &&
        !!!!!!condition == !!!!true &&
        !!!!!!!condition == !!!!!true &&
        !!!!!!!!condition == !!!!!!true
        ) {
            cout << "yes, good" << endl;
        }
    return 0;
}
