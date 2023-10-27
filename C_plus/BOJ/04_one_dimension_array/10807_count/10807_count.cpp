# include <iostream>

using namespace std;

int main()
{
  int N, v, arr[101], result = 0;

  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> arr[i];
  }
  cin >> v;

  for (int i = 0; i < N; i++)
  {
    if (arr[i] == v)
    {
      result += 1;
    }
  }

  cout << result;

  return 0;
}