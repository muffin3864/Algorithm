#include <iostream>

using namespace std;

int main()
{
  // 주어진 단어에서 가장 많이 사용된 알파벳을 대문자로 출력.
  // 가장 많이 사용된 알파벳이 여러 개인 경우 ?를 출력

  int alpha[26] = {0}, cnt = 0;
  string text;

  cin >> text;

  // 텍스트의 알파벳 별로 alpha배열에 카운트해서 집어넣기
  for (int i = 0; i < text.length(); ++i)
  {
    // 대문자
    if (text[i] < 97)
    {
      alpha[text[i] - 65]++;
    }

    // 소문자
    else
    {
      alpha[text[i] - 97]++;
    }
  }

  // 순회하면서 제일 많이 나온 값 찾기
  int max = 0, max_index = 0;
  for (int i = 0; i < 26; ++i)
  {
    if (max < alpha[i])
    {
      max = alpha[i];
      max_index = i;
    }
  }

  // 순회하면서 많이 나온 값이 여러개 인지 확인
  for (int i = 0; i < 26; ++i)
  {
    if (max == alpha[i])
    {
      cnt++;
    }
  }

  // 여러개면 "?" 출력, 아니면 대문자 출력
  if (cnt > 1)
  {
    cout << "?";
  }
  else
  {
    cout << char(max_index + 65);
  }

  return 0;
}