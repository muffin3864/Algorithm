#include <iostream>

using namespace std;

// 2차원 배열에서 세로 기준으로 차례대로 출력

int main()
{
  string arr[5];

  for (int i = 0; i < 5; ++i)
  {
    cin >> arr[i];
  }

  for (int i = 0; i < 15; ++i)
  {
    for (int j = 0; j < 5; ++j)
    {
      if (i < arr[j].size())
      {
        cout << arr[j][i];
      }
    }
  }

  return 0;
}