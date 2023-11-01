# include <iostream>

using namespace std;

int main()
{
  int N, M;

  cin >> N >> M;

  int arr[N + 1] = {0,};

  int i, j, k;
  for (int a = 0; a < M; a++)
  {
    cin >> i >> j >> k;
    for (int num = i; num <= j; num++)
    {
      arr[num] = k;
    }
  }
  
  for (int l=1; l <= N; l++)
  {
    cout << arr[l] << " ";
  }

  return 0;
}