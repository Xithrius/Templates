#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double C;
    cout << "Fahrenheit" << "  " << "Celsius" << endl;
    for (double F = 40; F <= 60; F++) {
       C = (F - 32) * (5.0 / 9);
       cout << fixed << setprecision(1) << F;
       cout << "          ";
       cout << fixed << setprecision(1) << C << endl;
    }
    return 0;
}
