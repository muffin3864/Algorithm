# include <iostream>

using namespace std;

int main()
{
  int X, N, a, b, result = 0;

  cin >> X;
  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> a >> b;
    result += a * b;
  }
  
  if (result == X)
  {
    cout << "Yes";
  }
  else
  {
    cout << "No";
  }
  
  return 0;
}