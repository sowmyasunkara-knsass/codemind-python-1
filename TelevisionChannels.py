#include <stdio.h>

int main(void) {
	int n;
	scanf("%d",&n);
	int i;
	int c=0;
	for(i=1;i<=n;i++)
	{
	    if(i%2!=0)
	    {
	        c=c+1;
	    }
	}
	printf("%d",c);
}
