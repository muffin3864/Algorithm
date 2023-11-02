#include <iostream>

using namespace std;

int main()
{
  string S;
  string alphabet = "abcdefghijklmnopqrstuvwxyz";
  cin >> S;

  for (int i = 0; i < alphabet.length(); i++)
  {
    cout << (int)S.find(alphabet[i]) << " ";
  }

  return 0;
}