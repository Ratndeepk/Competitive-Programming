//https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/

 #include<bits/stdc++.h>
 using namespace std;
class Solution
{   
public:     
    vector<int> spirallyTraverse(vector<vector<int> > matrix, int r, int c) 
    {
        int row = 0;
        int col = 0;
        vector<int> output;
        
        while(row<r && col<c)
        {
           //Printing 1st row
           for(int i=col; i<c; i++)
               output.push_back(matrix[row][i]);
           row++;
           //Printing last col
           for(int i=row; i<r; i++)
               output.push_back(matrix[i][c-1]);
           c--;
           //Printing last row
            if(row<r){
                for(int i=c-1; i>=col; --i)
                    output.push_back( matrix[r-1][i]);
                r--;
            }
           //Printing first col
            if(col<c){
                for(int i=r-1; i>=row; --i)
                    output.push_back( matrix[i][col]);
                col++;    
            }   
           
        }
        return output;
    }
};