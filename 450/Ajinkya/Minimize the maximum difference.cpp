
class Solution{   
public:
    int getMinDiff(int arr[], int n, int k) {
        if(n<=1)
          return 0;
        sort(arr,arr+n);

    int min_diff = arr[n-1]-arr[0];

    for(int i=1;i<n;i++)
    {
    	if(arr[i]-k<0)
    	continue;
	
    	int min_ele=min(arr[i]-k,arr[0]+k);
    	
    	int max_ele=max(arr[i-1]+k,arr[n-1]-k);
	
    	min_diff=min(min_diff,max_ele-min_ele); 
    }
    return min_diff;
    }
};
