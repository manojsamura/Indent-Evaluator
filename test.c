#include<stdio.h>
#include<stdlib.h>
void isbalanced(char *expr)
{
	char stack[50];
	int arr[50];
	int i,pos,k=0;

	int top=-1;
	for(i=0;expr[i]!=NULL;i++)
	{
		if(expr[i]=='[')
		{
			top++;
			stack[top]=expr[i];
                        
                        
                        
		}
		else if(expr[i]==']')
		{ 
                        
                        
			  if(stack[i]=='[')
	                    {top--;}
			else
			{
                            pos=i;
			    arr[k]=pos;
                            k++;
			}}
		if(expr[i]=='{')
		{
			top++;
			stack[top]=expr[i];
                     
		}
		else if(expr[i]=='}')
		{
                        
			if(stack[top]=='{')
	                 {
				top--;}
			else
			{
				pos=i;
                                arr[k]=pos;
                                k++;
			}
		}
	}

	if(top=-1)
          printf("All brackets matched!!\n");
	else
            {
	
		printf("Unmatched brackets at:");
                for(i=0;i<100;i++)
                 printf("%d",arr[k]);
		

	   } 

}

int main()
{
	char exprr[100];
	int i,n;
	/*printf("Enter the limit of the expression\n");
	  scanf("%d",&n);*/
	printf("Enter the expression to be checked\n");
	/* for(i=0;i<n;i++)
	   scanf("%c",&exprr[i]);*/
	gets(exprr);
	isbalanced(&exprr);
	return 0;
}



