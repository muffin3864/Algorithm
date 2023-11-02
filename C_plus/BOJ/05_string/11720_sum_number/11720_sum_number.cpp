#include <iostream>

using namespace std;

int main()
{
  int N, sum_num = 0;
  string number;

  cin >> N;
  cin >> number;

  for (int i = 0; i < N; i++)
  {
    sum_num += number[i] - '0';
  }

  cout << sum_num;

  return 0;
}