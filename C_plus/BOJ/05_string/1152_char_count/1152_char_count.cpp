#include <iostream>
#include <string>

using namespace std;

int main()
{
  int result = 1;
  string text;
  getline(cin, text);

  for (int i = 0; i < text.length(); i++)
  {
    if (text[i] == ' ')
    {
      result++;
    }
  }
  
  if (text[0] == ' ')
  {
    result--;
  }

  if (text[text.length() - 1] == ' ')
  {
    result--;
  }

  cout << result;

  return 0;
}