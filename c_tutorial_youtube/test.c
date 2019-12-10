#include<stdio.h>


void fonctionArray(int localEntierArray[]) 
{
	printf("%p\n", &localEntierArray[0]); 
  	return; 
} 
   
int main() 
{ 
	int entierArray[] = {0, 1, 2, 3};
	fonctionArray(entierArray);
  	printf("%p\n", &entierArray[0]);
  	return 0; 
}