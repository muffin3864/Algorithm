#include <iostream>
#include <string>

using namespace std;

int main()
{
  string text;

  while (true)
  {
    if (cin.eof())
    {
      break;
    }
    getline(cin, text);
    
    cout << text << "\n";
  }
  return 0;
}