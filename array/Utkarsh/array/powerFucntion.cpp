//https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
#include<bits/stdc++.h>
using namespace std;

int power(int x, unsigned int y, int p)  
{
  int result=1;
  x %= p;
  while(y){
    if(y&1) result*=x;
    y=y>>1;
    x = (x*x)%p;
  }
  return result;
}

int main()  
{  
    int x = 2;  
    int y = 5;  
    int p = 13;  
    cout << "Power is " << power(x, y, p);  
    return 0;  
}  