# include <iostream>

using namespace std;

int main()
{
    long long A, B, C;  // 10^12 * 3일 경우 int 자료형의 범위를 초과하므로 더 큰 범위인 long long으로 변수 선언

    cin >> A >> B >> C;

    cout << A + B + C;

    return 0;
}