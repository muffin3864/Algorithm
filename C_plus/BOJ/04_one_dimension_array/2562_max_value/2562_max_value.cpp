# include <iostream>

using namespace std;

int main()
{
  int arr[9], maxValue = -1, maxIndex;

  

  for (int i = 0; i < 9; i++)
  {
    cin >> arr[i];
  }
  
  for (int i = 0; i < 9; i++)
  {
    if (arr[i] > maxValue)
    {
      maxValue = arr[i];
      maxIndex = i;
    }
  }
  
  cout << maxValue << "\n";

  cout << maxIndex + 1;

  return 0;
}