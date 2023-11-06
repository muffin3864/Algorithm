#include <iostream>

using namespace std;

int main()
{
  string text;
  cin >> text;

  for (int i = 0; i < text.length() / 2; ++i)
  {
    if (text[i] != text[text.length() - i - 1])
    {
      cout << "0";
      return 0;
    }
  }

  cout << "1";
    
  return 0;
}