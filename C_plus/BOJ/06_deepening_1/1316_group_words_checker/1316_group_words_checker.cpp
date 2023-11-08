#include <iostream>

using namespace std;

int main()
{
  // 각 문자가 연속해서 나타나면 그룹 단어
  // 그룹 단어의 개수 출력
  int T, result = 0;
  
  cin >> T;

  // 주어진 단어 만큼 반복
  for (int i = 0; i < T; ++i)
  {
    string word;
    cin >> word;

    // 뒤에 한번더 같은 문자가 오는것을 체크할 boolean
    bool check = true;
    
    // 문자 전체를 순회
    for (int j = 0; j < word.length(); ++j)
    {
      //이미 지나온 문자들을 한 번 더 순회
      for (int k = 0; k < j; ++k)
      {
        // 현재 문자의 앞의 문자와 다르면서, 이전에 나온 적이 있는 문자이면
        if (word[j] != word[j - 1] && word[j] == word[k])
        {
          check = false;  // false로 체크 변경
          break;
        }
      }
    }
    
    // 문자가 한 번 더 나오지 않았으면 +1
    if (check == true)
    {
      result += 1;
    }

  }

  // 결과값 출력
  cout << result;

  return 0;
}