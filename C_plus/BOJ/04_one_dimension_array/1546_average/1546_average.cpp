# include <iostream>
# include <algorithm>

using namespace std;

int main()
{
  int N;
  cin >> N;

  int scores[N];
  for (int i = 0; i < N; i++)
  {
    cin >> scores[i];

    // cout << scores[i];
  }
  int size = sizeof(scores) / sizeof(*scores);

  float max = *std::max_element(scores, scores + size);

  float new_scores[N], sum = 0;
  for (int i = 0; i < N; i++)
  {
    new_scores[i] = (scores[i] / max) * 100;

    // cout << new_scores[i] << " ";

    sum += new_scores[i];
  }
  
  float avg = sum / N;

  cout << avg;
  
  return 0;
}