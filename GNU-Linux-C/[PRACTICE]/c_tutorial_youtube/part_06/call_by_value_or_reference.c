#include <stdio.h>

int globalVar = 1;
int  globalArray[] = {1, 2, 3};

void checkValueOrReference(int arg_var, int arg_array[])
{
	//printf("int variable address: %p\n", &globalVar);
	//printf("Local int variable address: %p\n", &arg_var);

	//printf("int array address: %p\n", &globalArray);
	//printf("Local int array address: %p\n", &arg_array);

	arg_var = 4;
	arg_array[2] = 4;

	printf("Local int value: %d\n", arg_var);
	printf("Local array value at index 2: %d\n", arg_array[2]);
}

int main(void)
{
	checkValueOrReference(globalVar, globalArray);

	printf("Global int value: %d\n", globalVar);
	printf("Global array value at index 2: %d\n", globalArray[2]);

	return 0;
}