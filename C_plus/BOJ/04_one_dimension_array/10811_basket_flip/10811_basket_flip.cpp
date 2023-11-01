# include <iostream>

using namespace std;

int main()
{
  int N, M;

  cin >> N >> M;

  int arr[N + 1];
  for (int i = 1; i < N + 1; i++)
  {
    arr[i] = i;
  }

  int i, j;
  for (int a = 0; a < M; a++)
  {
    cin >> i >> j;

    for (int b = 0; b <= (j - i) / 2; b++)
    {
      swap(arr[i + b], arr[j - b]);
    }
  }

  for (int i = 1; i < N + 1; i++)
  {
    cout << arr[i] << " ";
  }

  return 0;
}