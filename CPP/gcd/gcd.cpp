#include <iostream>
using std::cout;
using std::endl;

int gcd(int &a, int &b)
{
  int tmp;
  
  while (a != 0)
  {
    if (a < b)
    {
      tmp = a;
      a = b;
      b = tmp;
    }
    else 
    {
      a -= b;
    }
  }
  return b;
}

int main() 
{
  int x = 280;
  int y = 30;
  int res = gcd(x, y);
  cout << res << endl;
}