#include<stdio.h>

int main()
{
    int n;
    scanf("%d\n", &n);
    int i,j,m[n][n],sum1=0,sum2=0,result=0;
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            scanf("%d",&m[i][j]);
        }
    }
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            //printf("%d ",m[i][j]);
            if (i==j)
            {
                sum1 = sum1+m[i][j];
            }
        }
        //printf("\n");
    }

    j = n-1;
    for(i=0; i<n; i++)
    {
        while(j>=0)
        {
            sum2 += m[i][j];
            break;
        }
        j--;
    }

    //printf("%d\n",sum1);
    //printf("%d\n",sum2);
    if((sum1-sum2)<0)
    {
        result = -1*(sum1-sum2);
    }
    else
    {
        result = sum1-sum2;
    }
    printf("%d",result);
    return 0;
}
