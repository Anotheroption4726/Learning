#include <stdio.h>

#define MAX 10


int main(void)
{
	int inputData[MAX];
	int tmpNum;
	FILE *fp;

	fp = fopen("input.txt", "r");

	if(fp == NULL)
	{
		printf("Could not open file.\n");
		return(0);
	}

	for (int i = 0; i < MAX; i++)
	{
		fscanf(fp, "%d", &inputData[i]);
	}

	fclose(fp);

	for (int i = 0; i < MAX; i++)
	{
		for (int j = 0; j < MAX; j++)
		{
			if (inputData[i] < inputData[j])
			{
				tmpNum = inputData[i];
				inputData[i] = inputData[j];
				inputData[j] = tmpNum;
			}
		}
	}

	fp = fopen("output.txt", "w");

	if(fp == NULL)
	{
		printf("Could not open output.txt for writting.\n");
		return(0);
	}
	
	fprintf(fp, "\nSorted data:\n");

	for(int i = 0; i < MAX; i++)
	{
		fprintf(fp, "item #%d: %d\n", i + 1, inputData[i]);
	}

	fclose(fp);

	return(0);
}