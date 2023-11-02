#include <iostream>

using namespace std;

int main()
{
  int T, R;
  string text, repeat;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    cin >> R >> text;

    for (int i = 0; i < text.length(); i++)
    {
      for (int j = 0; j < R; j++)
      {
        cout << text[i];
      }
    }
    cout << "\n";
  }

  return 0;
}