//https://leetcode.com/problems/find-the-duplicate-number/solution/
#include<bits/stdc++.h>
using namespace std;
//if only one duplicate is present below solution would work,
// it uses xor operator to find the single duplicate element, derived from MissingElementQuestion;
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int expected=0,actual=0;
        for(int i=1;i<nums.size();i++)
            expected = expected^i;
        
        for(int i=0;i<nums.size();i++)
            actual =actual ^ nums[i];
        
        return expected^actual;
    }
};

// Floyd cycle finding algorithm

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
    int tortoise = nums[0];
    int hare = nums[0];
    do{
      tortoise=nums[tortoise];
      hare=nums[nums[hare]];
    }while(tortoise!=hare);
    
    tortoise=nums[0];
    while(tortoise!=hare){
      tortoise=nums[tortoise];
      hare=nums[hare];
    }
  return hare;
  }
};