#include "stack.hpp"

const int max_input = 6;

int main() {
	stack turner;
	ELEMENT user_input;
	for (int loop = 1; loop < max_input; loop++)
	{
		cout<<"Iuput node."<<loop<<": ";
		cin>>user_input;
		turner.push(user_input);
	}
	turner.display();

	for (int i = 0; i < max_input; i++)
	{
		if (!turner.is_empty()) {
			user_input = turner.get_top();
			turner.pop();
			cout<<"Output node."<<i<<": ";
			cout<<user_input<<"\n";
		}
	}
	if (turner.is_empty())
	{
		cout<<"now, stack is NULL";
	}

	return 1;
}