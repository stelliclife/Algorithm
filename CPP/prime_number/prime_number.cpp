#include <iostream>
using std::cout;
using std::endl;

bool is_prime_number01(const int &n)
{
  for(int i=2; i<n; i++)
  {
    if(n % i != 0)
      continue;
    if (i != n)
      return false;
  }
  return true;
}

bool is_prime_number02(const int &n)
{
  int m = (int)sqrt(n);
  for(int i = 2; i < m; i++)
  {
    if(n % i != 0)
      continue;
    if(i != n)
      return false;
  }
  return true;
}

int main()
{
  cout << "Prime Number: " << is_prime_number01(100) << endl;
  cout << "Prime Number: " << is_prime_number02(11) << endl;
  return 0;
}