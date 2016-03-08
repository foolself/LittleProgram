#include "stack.hpp"
#include <stdlib.h>
stack::stack() {
	top = NULL;
	return;
}

stack::~stack() {
	NODE * ptr;

	while (top != NULL) {
		ptr = top;
		top = top -> link;
		delete ptr;
	}

	return;
}

void stack::push(ELEMENT obj) {
	NODE * temp;

	temp = new NODE;
	if (temp != NULL)
	{
		temp -> link = top;
		temp -> element = obj;
		top = temp;
	} else {
		cout<<"Error: No enough memory. \n";
		exit(1);
	}
}

void stack::pop() {
	NODE * temp;

	if (top != NULL)
	{
		temp = top;
		top = top -> link;
		delete temp;
	} else {
		cout<<"Error: Pop from empty stack. \n";
		exit(1);
	}
}

ELEMENT stack::get_top() {
	if (top == NULL)
	{
		cout<<"Error: Get top from empty stack. \n";
		exit(1);
	}
	return top -> element;
}

int stack::is_empty() {
	return (top == NULL);
}

void stack::display() {
	NODE * loop;

	loop = top;
	while (loop != NULL) {
		cout<<loop -> element<<" ";
		loop = loop -> link;
	}
	cout<<"\n";
	return;
}