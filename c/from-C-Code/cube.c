 //Print 1 to 10 using do while loop in C - program example


#include<stdio.h>

int main(){

	/* Initialize starting number */
	int a = 1;

	/* Initialize target number */
	int b = 10;

	//Start do while loop
	 do{
		 

		printf("%d\n", a);

		//increment the number by 1
		++a;

		//once number is > target in while condition
		//then control will be out of loop
	 }while (a <= b);

	return 0;
}