#include <stdio.h>
#include <string.h>
int hextoten(char a[5]) {
	int i,num;
	char ch;
	num=0;
	for(i=0;i<5;i++) {
		ch=a[i];
		if((ch=='H')||(ch=='\0')) break;
		if ((ch>=0)&&(ch<='9')) 
			ch=ch-'0';
		else ch=ch-'0'-7; num=num*16+ch;
	}
	return(num);
}

char *strupr(char *str) 
{ 
	char *ptr = str; 

	while (*ptr != '\0') { 
		if (islower(*ptr)) 
			*ptr = toupper(*ptr); 
		ptr++; 
	} 

	return str; 
}

void main() {
	char strhex[5]="100";
	int numten,k;
	strupr(strhex);
	numten=hextoten(strhex);
	printf("NUM=%d\n",numten);
}