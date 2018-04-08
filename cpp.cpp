#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    cout << "Hello World from cpp!\n";
    cout << (argc - 1) << " Args: [";
    for (int i = 1; i < argc; ++i)
        cout << argv[i] << " ";
    cout << "]\n";
    return 0;
}
