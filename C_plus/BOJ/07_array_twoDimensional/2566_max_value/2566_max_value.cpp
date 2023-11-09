#include <iostream>

using namespace std;

// 9x9 격자판에 쓰여진 숫자중
// 최대값을 찾고 최대값의 index 출력

int main()
{
  int arr[9][9], max_value = 0, max_i_index = 0, max_j_index = 0;

  for (int i = 0; i < 9; ++i)
  {
    for ( int j = 0; j < 9; ++j)
    {
      cin >> arr[i][j];

      if (max_value < arr[i][j])
      {
        max_value = arr[i][j];

        max_i_index = i;

        max_j_index = j;
      }
    }
  }

  cout << max_value << "\n";
  cout << max_i_index + 1 << " " << max_j_index + 1;

  return 0;
}