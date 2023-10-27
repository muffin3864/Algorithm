# include <iostream>

using namespace std;

int main()
{
  int T, A, B, C;

  cin >> T;

  for (int i = 1; i < T + 1; i++)
  {
    cin >> A >> B;

    C = A + B;

    cout << "Case #" << i << ": " << A << " + " << B << " = " << C << endl;
    
  }
  return 0;
}