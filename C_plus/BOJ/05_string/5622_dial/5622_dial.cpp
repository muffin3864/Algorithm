#include <iostream>

using namespace std;

int main()
{
  int time = 0, dial[] = {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10};
  string text;

  cin >> text;

  for (int i = 0; i < text.length(); ++i)
  {
    time += dial[text[i] - 65];
  }

  cout << time;

  return 0;
}