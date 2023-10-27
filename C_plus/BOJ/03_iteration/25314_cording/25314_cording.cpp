# include <iostream>

using namespace std;

int main()
{
  int N, cnt;

  cin >> N;

  cnt = N / 4;

  for (int i = 0; i < cnt; i++)
  {
    cout << "long" << " ";
  }
  cout << "int";
  return 0;
}