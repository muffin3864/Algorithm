#include <iostream>

using namespace std;

int main()
{
  string A, B, new_A, new_B;

  cin >> A >> B;

  for (int i = 2; i >= 0; --i)
  {
    new_A += A[i];
    new_B += B[i];
  }
  cout << max(new_A, new_B);

  return 0;
}