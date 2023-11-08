#include <iostream>

using namespace std;

// 전공 평점이 3.3이상이면 졸업 가능.
// 전공 평점 = 전공 과목별(학점 x 과목평점)의 합 / 학점 총합
// 등급이 p인 경우는 계산에서 제외

int main()
{
  double sumCredit = 0.0, res = 0.0, credit, temp;
  string name, grade;

  for (int i = 0; i < 20; ++i)
  {
    cin >> name >> credit >> grade;

    if (grade == "P")
    {
      continue;
    }
    sumCredit += credit;

    if (grade == "F")
    {
      continue;
    }

    if (grade[0] == 'A')
    {
      temp = 4;
    }
    else if (grade[0] == 'B')
    {
      temp = 3;
    }
    else if (grade[0] == 'C')
    {
      temp = 2;
    }
    else
    {
      temp = 1;
    }

    if (grade[1] == '+')
    {
      temp += 0.5;
    }

    res += credit * temp;
  }

  cout << res / sumCredit;

  return 0;
}