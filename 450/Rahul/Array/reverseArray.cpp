#include <iostream>
using namespace std;

int main(){

	int n,temp; 
	cin >> n;
	int a[n], end = n-1;
	for ( int i = 0; i < n; i++ )
		cin>>a[i];
	for ( int i = 0; i < n/2; i++ ){
		temp = a[i];
		a[i] = a[end];
		a[end--] = temp;
	}
	for ( int i = 0; i < n; i++ )
		cout << a[i] << " ";
	return 0;
}
