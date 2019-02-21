#include <bits/stdc++.h>
using namespace std;

int main()
{
    //check the enterd number is perfect or not
    int a,i,sum,b,c,j;
    /*while(1)
    {
        printf("Enter a number to check perfect or not: ");
        scanf("%d/n",&a);
        i=1;
        sum=0;
        while(i<a)
        {
            if(a%i==0)
            {
                sum = sum+i;
            }
            i++;
        }
        if(sum==a)
        {
            printf("The entered number is a perfect number.\n");
        }
        else
        {
            printf("The entered number is not a perfect number.\n");
        }
    }*/

    //check the enterd number is perfect or not within given range

    printf("enter the max and min range: ");
    scanf("%d %d",&b,&c);
    printf("The perfect numbers between the range is: \n");

    for(j=b; j<=c; j++)
    {
        i=1;
        sum=0;
        while(i<j)
        {
            if(j%i==0)
            {
                sum = sum+i;
            }
            i++;
        }
        if(sum==j)
        {
            printf("%d\n",j);
        }
    }
    return 0;
}
