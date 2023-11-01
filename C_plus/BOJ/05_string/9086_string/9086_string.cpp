#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    string text;
    cin >> text;

    cout << text[0] << text[text.length() - 1] << "\n";
  }
  return 0;
}