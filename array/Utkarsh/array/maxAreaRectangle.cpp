//https://practice.geeksforgeeks.org/problems/max-rectangle/1

#include<bits/stdc++.h>
using namespace std;
#define MAX 1000
int getArea(int hist[], int n) {
    stack<int> s; 
    int max_area = 0; 
    int tp;  
    int area_with_top; 
    int i = 0; 
    while (i < n) 
    { 
        if (s.empty() || hist[s.top()] <= hist[i]) 
            s.push(i++); 
        else{ 
            tp = s.top(); 
            s.pop();
            area_with_top = hist[tp]*(s.empty()?i:i-s.top()-1); 
            if (max_area < area_with_top) 
                max_area = area_with_top; 
        } 
    } 
    while (s.empty() == false) 
    { 
        tp = s.top(); 
        s.pop(); 
        area_with_top = hist[tp]*(s.empty()?i:i-s.top()-1); 
        if (max_area < area_with_top) 
            max_area = area_with_top; 
    } 
    return max_area; 
}
 
int maxArea(int M[MAX][MAX], int n, int m) {
    int res = getArea(M[0], m);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) 
            if (M[i][j]) M[i][j] += M[i-1][j];
        res = max(res, getArea(M[i], m));
    }
    return res;
}
