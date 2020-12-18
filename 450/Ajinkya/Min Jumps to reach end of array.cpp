int minJumps(int arr[], int n){
     int* jumps = new int[n];
    int i, j;
 
    if (n == 0 || arr[0] == 0)
        return -1;
 
    jumps[0] = 0;
 
    for (i = 1; i < n; i++) {
        int flag=0;
        jumps[i] = INT_MAX;
        for (j = 0; j < i; j++) {
            if (i <= j + arr[j] && jumps[j] != INT_MAX) {
                jumps[i] = min(jumps[i], jumps[j] + 1);
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            jumps[i]=-1;
        }
    }
    return jumps[n - 1];
}
