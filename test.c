#include<stdio.h>
int main()
{
    /*while(1)
    {
        int base,height;
        float area;
        scanf("%d %d",&base,&height);
        //base = 10;
        //height = 15;

        //area = (base*height)/2;
        //printf("%d",area);
        area = (float)(base*height)/2;
        printf("the area of the triangle is: %f",area);
    }*/

    int a = 80, b=40, c=15;
    /*for(a=10;a>0;a--)
    {
        printf("%d\n",a);
    }*/

    /*while(a>=-100)
    {
        printf("%d\n",a);
        a--;
    }*/

    /*do
    {
      printf("%d\n",a);
        a--;
    }
    while(a>200);*/

    if((a>=80) && (b>=80) && (c>=80))
    {
        printf("A+");
    }
    else if((a>=80) && (b>=40) || (c>=40))
    {
        printf("pass");
    }
    else
    {
        printf("fail");
    }

}
