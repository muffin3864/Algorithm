# include <iostream>

using namespace std;

int main()
{
  int h, m, time;
  cin >> h >> m;
  cin >> time;

  h += time / 60;
  m += time % 60;

  if (m >= 60)
  {
    h += 1;
    m -= 60;
  }

  if (h >= 24)
  {
    h -= 24;
  }
  

  cout << h << " " << m;

  return 0;
}