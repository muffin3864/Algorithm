#include <iostream>

using namespace std;

int main()
{
  int arr[6] = {1, 1, 2, 2, 2, 8};
  int my_chess[6];

  for (int i = 0; i < 6; ++i)
  {
    cin >> my_chess[i];
  }

  for (int i = 0; i < 6; ++i)
  {
    arr[i] -= my_chess[i];
  }

  for (int i = 0; i < 6; ++i)
  {
    cout << arr[i] << " ";
  }

  return 0;
}