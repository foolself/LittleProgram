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

int culMonthFirstDay(int preMonthFirstDay, int preMonthdays) {
	int monthFirstDay;
	monthFirstDay = (preMonthFirstDay + preMonthdays) % 7;
	return monthFirstDay;
}	

void main()
{
	int i, j, k, count;
	int weekFlag1, weekFlag2;
	int day1, day2;
	int firstDays[12];
	firstDays[0] = 5;
	for (i = 1; i < 12; i++)
	{

		firstDays[i] = culMonthFirstDay(firstDays[i - 1], days(i));
	}

	for (i = 0; i < 6; i++)
	{
		day1 = day2 = 1;
		weekFlag1 = firstDays[2 * i];
		weekFlag2 = firstDays[2 * i + 1];
		printf("========= %s 2016 =========", months[2 * i]);
		printf("      ");
		printf("========= %s 2016 =========", months[2 * i + 1]);
		printf("\n");
		printf(" SUN MON TUE WED THU FRI SAT");
		printf("      ");
		printf(" SUN MON TUE WED THU FRI SAT");
		printf("\n");
		for (j = 0; j < 6; j++)
		{
			if (day1 == 1 && weekFlag1 != 7)
			{
				for (k = 0; k < weekFlag1; k++)
				{
					printf("    ");
				}
			}
			while (weekFlag1 < 7 && day1 < days(2 * i + 1) + 1)
			{
				if (day1 < 10)
				{
					printf(" ");
				}
				printf("  %d", day1);
				day1++;
				weekFlag1++;
			}
			for (k = 0; k < 7 - weekFlag1;k++)
			{
				printf("    ");
			}
			printf("      ");

			if (day2 == 1 && weekFlag2 != 7)
			{
				for (k = 0; k < weekFlag2; k++)
				{
					printf("    ");
				}
			}
			while (weekFlag2 < 7 && day2 < days(2 * i + 2) + 1)
			{
				if (day2 < 10)
				{
					printf(" ");
				}
				printf("  %d", day2);
				day2++;
				weekFlag2++;
			}

			weekFlag1 = weekFlag2 = 0;
			printf("\n");
		}
		printf("\n");
	}


}