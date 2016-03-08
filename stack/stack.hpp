#include <iostream>

using namespace std;
typedef int ELEMENT;

struct NODE {
	ELEMENT element;
	NODE * link;
};

class stack {
public:
	stack();
	~stack();

	void push(ELEMENT obj);
	void pop();

	ELEMENT get_top();

	int is_empty();

	void display();
private:
	NODE * top;
};