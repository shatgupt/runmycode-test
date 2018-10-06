/*
  This program won't run properly without an input.
  Try with: abc
*/
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    cout << "Hello World from C++!\n";
    string mystr;
    getline(cin, mystr);
    cout << mystr << "\n";
    return 0;
}

