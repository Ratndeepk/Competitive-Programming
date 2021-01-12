//https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
#include <bits/stdc++.h> 
using namespace std; 

#define ll long long
#define loop for(int i = 0; i < n; i++) 
#define looop(i, n) for (int i = 0; i < n; i++) 
#define loopp(i, k, n) for (int i = k; k < n? i < n: i > n; k < n? i += 1: i -= 1) 
#define dbug(x) cout << #x << "=" << x << endl
#define debug(x, y) cout << #x << "=" << x << ", " << #y << "=" << y << endl
#define pb push_back
#define mp make_pair
#define clr(x) memset(x, 0, sizeof(x))
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define trav(a) for (auto it = a.begin(); it != a.end(); it++)
#define endl "\n"
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pi> vpi;
typedef vector<vi> vvi;
#define ending first.second 
#define pos second
#define start first.first


bool comparator(pair<pi,int> &a, pair<pi,int> &b){
     if (a.first.second != b.first.second) {
        return a.ending < b.ending;
    }
    // If the finish times are same , then sort according to their previous position
    return (a.pos < b.pos);
}
void maxMeetings(int s[], int f[], int n) {
    
    vector<pair<pi,int>> rat(n);
    
    for (int i = 0; i < n; i++){ 
		rat[i].start = s[i];
		rat[i].ending = f[i];  
		rat[i].pos = i + 1; 
	} 
    sort(rat.begin(), rat.end(), comparator); 
    vector<int> m;
    int timeLimit = rat[0].ending;
    
    cout<<rat[0].pos<<" ";
    for(int i =1 ;i< n;i++)
        if (rat[i].start > timeLimit){
            m.pb(rat[i].pos);
            timeLimit = rat[i].ending;
        }
    trav (m) cout<<*it<<" ";
}