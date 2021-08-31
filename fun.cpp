#include <iostream>
using namespace std;
string input(string q) {
    string a;
    cout << q;
    cin >> a;
    return a;
}
void print(int p[], int a) {
    cout << '[';
    unsigned int j;
    for (j = 0;j < a - 1;j++) { cout << p[j] << ", "; }
    cout << p[j] << "]\n";
}
int randint(int lower, int upper) {
    return ((rand() % (upper - lower + 1)) + lower);
}
int main() {
    srand(time(NULL));
    int n = stoi(input("Enter a number: "));
    int list[n];
    for (int i = 0;i < n;i++) { list[i] = randint(0,n); }
    print(list, n);
}