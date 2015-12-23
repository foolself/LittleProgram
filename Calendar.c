// 1, Jan is Fri
#include "stdio.h"

char * months[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

int days(int month) {
	int count = 30;
	if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month ==12) {
		count = 31;
	}
	if (month == 2)
	{
		count = 29;
	}
	return count;
}

void main() {
	int i, j, k, count;
	int weekFlag = 5;
	for (i = 0; i < 12; i++)
	{
		count = days(i + 1);
		printf("========= %s 2016 =========\n", months[i]);
		printf("   S   M   T   W   T   F   S\n");
		if (weekFlag != 7) {
			for (k = 0; k < weekFlag; k++)
			{
				printf("    ");
			}
		}
		for (j = 0; j < count; j++)
		{
			if (weekFlag == 7)
			{
				printf("\n");
			}
			if (j + 1 < 10)
			{
				printf(" ");
			}
			printf("  %d", j + 1);
			weekFlag ++;
			if (weekFlag == 8)
			{
				weekFlag = 1;
			}
		}
		printf("\n\n");
	}
	printf("\n");
}