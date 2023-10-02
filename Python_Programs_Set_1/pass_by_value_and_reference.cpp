#include<stdio.h>

void func1(int u, int v);
void func2(int *pu, int *pv);

void func1(int u, int v)
{
	u=0;
	v=0;
	
	printf("\nWithin func1: u=%d, v=%d", u, v);
	return;
}

void func2(int *pu, int *pv)
{
	*pu=0;
	*pv=0;
	
	printf("\nWithin func2: *pu=%d, *pv=%d", *pu, *pv);
	
	return;
}


int main()
{
	int u =1;
	int v = 3;
	
	printf("\nBefore calling func1: u=%d, v=%d", u, v);
	func1(u, v);
	printf("\nAfter calling func1: u=%d, v=%d", u, v);
	
	printf("\n");
	
	printf("\nBefore calling func2:	u=%d, v=%d", u, v);
	func2(&u, &v);
	printf("\nAfter calling func2: u=%d, v=%d", u, v);
	
	
	return(0);
	
}
