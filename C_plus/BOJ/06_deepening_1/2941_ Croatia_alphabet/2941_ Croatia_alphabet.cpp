#include <iostream>

using namespace std;

int main()
{
  int index;
  string text, croa[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

  cin >> text;

  for (int i = 0; i < 8; ++i)
  {
    while (true)
    {
      index = text.find(croa[i]);

      if (index == string::npos)
      {
        break;
      }

      text.replace(index, croa[i].length(), "a");
    }
  }

  cout << text.length();

  return 0;
}