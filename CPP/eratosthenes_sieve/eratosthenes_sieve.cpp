#include <iostream>
using std::cout;
using std::endl;

void eratosthenes_sieve(int* arr, const int &n)
{
  int i = 2;
  int m = 2;
  while(i < n)
  {
    if (m <= n) 
    {
      if (arr[m-1] == 0)
        arr[m-1] = -1;
      m += i;
    }
    else
    {
      i++;
      m = i;
      m += i;
    }
  }
}

int main()
{
  const int n = 50;
  int arr[n] = {0};
  eratosthenes_sieve(arr, n);

  for (int i = 0; i < n; i++)
  {
    if (arr[i] != -1)
      cout << i + 1 << ", ";
  }
  cout << endl;
  return 0;
}