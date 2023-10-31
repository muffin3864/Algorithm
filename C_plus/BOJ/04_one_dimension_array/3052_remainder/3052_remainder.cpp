# include <iostream>

using namespace std;

int main()
{
  int A, result = 0, arr[42] = {};
  for (int i = 0; i < 10; i++)
  {
    cin >> A;

    arr[A % 42]++;
  }

  for (int i : arr)
  {
    if (i > 0)
    {
      result++;
    }
  }

  cout << result;

  return 0;
}