#include <stdio.h>

struct {
    $parameterType got;
    $returnType want;
}test_table[] = 
{
   //TODO-> write here your test cases
};

int main() {
    size_t n = sizeof(test_table)/sizeof(test_table[0]);
    
    for (int i=0; i<n; i++){
        if ( $funcName (test_table[i].got) == test_table[i].want ){
            printf("Test OK")
        }
    }
}