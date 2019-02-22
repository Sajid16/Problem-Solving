#include<bits/stdc++.h>
using namespace std;

int main()
{
    while(1)
    {
        int a,i,len=0,sum=0,c;
        float b,d;
        printf("Enter a number to check armstrong number or not: ");
        scanf("%d",&a);
        c=a;
        while(a!=0)
        {
            a= a/10;
            len++;
        }

        a=c;
        for(i=0; i<len; i++)
        {
            while(c!=0)
            {
                d=c%10;
                c=c/10;
                b=pow(d,len);//pow functon may be only accept float value
                //printf("%.0f\n",b);
                sum=sum+b;

            }
        }
        if(sum==a)
        {
            printf("%d is an armstrong number\n",a);
        }
        else
        {
            printf("%d is not an armstrong number\n",a);
        }
    }

    return 0;
}
