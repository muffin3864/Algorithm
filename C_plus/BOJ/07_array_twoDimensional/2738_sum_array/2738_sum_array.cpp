#include <iostream>

using namespace std;

// N x M 행렬 A, B
// A + B 를 출력

int main()
{
  int N, M;

  cin >> N >> M;

  int A[N][M], B[N][M];

  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < M; ++j)
    {
      cin >> A[i][j];
    }
  }

  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < M; ++j)
    {
      cin >> B[i][j];
    }
  }

  for (int i = 0; i < N; ++i)
  {
    for (int j = 0; j < M; ++j)
    {
      cout << A[i][j] + B[i][j] << " ";
    }
    cout << "\n";
  }

  return 0;
}