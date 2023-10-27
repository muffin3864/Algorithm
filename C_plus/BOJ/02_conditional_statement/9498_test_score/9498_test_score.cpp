# include <iostream>

using namespace std;

int main()
{
  int num;
  cin >> num;

  if (90 <= num)
  {
    cout << "A";
  }

  else if (80 <= num)
  {
    cout << "B";
  }

  else if (70 <= num)
  {
    cout << 'C';
  }

  else if (60 <= num)
  {
    cout << 'D';
  }
  else
  {
    cout << 'F';
  }

  return 0;
}