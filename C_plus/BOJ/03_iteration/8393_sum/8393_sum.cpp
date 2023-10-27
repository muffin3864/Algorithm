# include <iostream>

using namespace std;

int main()
{
  int n, sum_num = 0;
  cin >> n;

  for (int i = 1; i <= n; i++)
  {
    sum_num += i;
  }

  cout << sum_num;
  return 0;
}