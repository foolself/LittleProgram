#include <stdio.h>
#include <ctype.h>
int hextoten(char a[5]) {
	int i,num;
	char ch;
	num=0;
	for(i=0;i<5;i++) {
		ch=a[i];
		printf("====== %d ====\n", i);
		printf("%c", ch);
		if((ch>='G')||(ch=='\0')) break;
		if ((ch>=0)&&(ch<='9')) {
			ch=ch-'0';
			printf("--->%d\n", ch);
		}
		else {
			ch=ch-'7';
			printf("--->%d\n", ch);
		}
		num=num*16+ch;
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
	char strhex[5]="7fff";
	int numten,k;
	// strupr(strhex);
	printf("%s\n", strupr(strhex));
	numten=hextoten(strhex);
	printf("NUM=%d\n",numten);
}
