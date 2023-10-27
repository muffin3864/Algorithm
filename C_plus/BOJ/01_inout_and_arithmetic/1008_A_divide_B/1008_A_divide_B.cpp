#include <iostream>

using namespace std;

int main()
{
    double A, B;                // float은 유효숫자 6자리 까지 나타내짐, double은 15자리
    cin >> A >> B;

    cout.precision(9);          // 출력 자리수 설정
    cout << fixed;              // 정수 상관 없이 소수점 아래 고정
    cout << A / B;
    // cout.unsetf(ios::fixed);    // 고정 해제

    return 0;
}