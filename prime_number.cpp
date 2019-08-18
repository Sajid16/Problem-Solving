#include<bits/stdc++.h>
using namespace std;

int main()
{
    int st,en,i,result[10000],j;

    printf("enter the starting node:\n");
    scanf("%d",&st);
    printf("enter the ending node:\n");
    scanf("%d",&en);

    printf("the prime numbers between the range of %d and %d is:\n",st,en);
    for(i=st; i<=en; i++)
    {
        int count = 0;
        for(j=2; j<=i/2; j++)
        {
            if(i%j == 0)
            {
                count++;
                break;
            }
        }

        if(count == 0 && i !=1)
        {
            printf("%d ",i);
        }
    }

    /*printf("the prime numbers between the range of %d and %d is:/n",st,en);
    for(j=0; j<en; j++)
    {
        printf("%d", result[j]);
    }*/

    return 0;
}
