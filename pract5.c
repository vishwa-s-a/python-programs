#include<stdio.h>
void main()
{
  int i,val=0,fact=1;
  //printf("Hello World");
  printf("Enter the number\n");
  scanf("%d",&val);
  for(i=1;i<=val;i++)
  {
    fact=fact*i;
  }
  printf("%d",fact);
}
