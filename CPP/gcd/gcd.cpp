#include <iostream>
using std::cout;
using std::endl;

int gcd01(int &a, int &b)
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

int gcd02(int &a, int &b)
{
    int tmp;

    while (a != 0)
    {
        tmp = a % b;
        a = b;
        b = tmp;
    }
    return b;
}

int main() 
{
  int x = 280;
  int y = 30;
  int res01 = gcd01(x, y);
  int res02 = gcd02(x, y);
  cout << "GCD01: " << res01 << " | GCD02: " << res02 << endl;
}