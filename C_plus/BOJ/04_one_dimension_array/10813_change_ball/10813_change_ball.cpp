# include <iostream>

using namespace std;

int main()
{
  int N, M;

  cin >> N >> M;

  int arr[N + 1];
  for (int i = 0; i <= N; i++)
  {
    arr[i] = i;
  }
  

  int a, b, num_a, num_b;
  for (int i = 1; i < M + 1; i++)
  {
    cin >> a >> b;

    num_a = arr[a];
    num_b = arr[b];

    arr[a] = num_b;

    arr[b] = num_a;
  }

  for (int i = 1; i <= N; i++)
  {
    cout << arr[i] << " ";
  }

  return 0;
}