#include <iostream>

using namespace std;

// 좌표가 주어지고 색종이를 여러 장 붙인다.
// 도화지의 크기는 가로, 세로 100이다.
// 색종이의 크기는 가로, 세로 10이다.
// 주어지는 좌표는 왼쪽아래의 한 좌표만 주어진다.
// 이후 색종이가 붙어있는 검은 영역의 넓이를 출력

int main() 
{
  int arr[101][101] = {0};
  int N, x, y, cnt = 0;

  cin >> N;

  for (int k = 0; k < N; k++)
  {
    cin >> x >> y;

    for (int i = x; i < x + 10; i++)
    {
      for (int j = y; j < y + 10; j++)
      {
        if (arr[i][j] == 0)
        {
          arr[i][j] = 1;
          cnt++;
        }
      }
    }

  }
  cout << cnt;

  return 0;
}



