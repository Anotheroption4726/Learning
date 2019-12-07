#include <stdio.h>

#define MAX 10


int main(void)
{
	int inputData[MAX];
	int tmpNum;

	for (int i = 0; i < MAX; i++)
	{
		printf("Enter value #%d :", i + 1);
		scanf("%d", &inputData[i]);
	}

	for (int i = 0; i < MAX; i++)
	{
		for (int j = 0; j < MAX; j++)
		{
			if (inputData[j] > inputData[i])
			{
				tmpNum = inputData[i];
				inputData[i] = inputData[j];
				inputData[j] = tmpNum;
			}
		}
	}

	for (int i = 0; i < MAX; i++)
	{
		printf("Value #%d : %d\n", i + 1, inputData[i]);
	}

	return(0);
}