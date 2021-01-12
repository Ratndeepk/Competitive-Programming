//https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

#include <iostream> 
using namespace std; 
# define NO_OF_CHARS 256 
  
class gfg 
{ 
    public : 
    void fillCharCounts(char *str, int *count) 
    { 
        int i; 
        for (i = 0; *(str + i); i++) 
        count[*(str + i)]++; 
    } 
    void printDups(char *str) 
    { 
        int *count = (int *)calloc(NO_OF_CHARS,   sizeof(int)); 
        fillCharCounts(str, count); 
  
        int i; 
        for (i = 0; i < NO_OF_CHARS; i++) 
        if(count[i] > 1) printf("%c, count = %d \n", i, count[i]); 
        free(count); 
    } 
}; 
  
int main() 
{ 
    gfg g ; 
    char str[] = "test string"; 
    g.printDups(str); 
    return 0; 
} 