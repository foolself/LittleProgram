#include <iostream>

void move_tower(int disk_num, char from, char to, char aux) {
	using namespace std;
	if (disk_num == 1)
	{
		cout<<"Move disk1 from "<<from<<" to "<<to<<"\n";
	} else {
		move_tower(disk_num - 1, from, aux, to);
		cout<<"Move disk"<<disk_num<<" from "<<from<<" to "<<to<<"\n";
		move_tower(disk_num - 1, aux, to ,from);
	}
	return;
}

int main() {
	move_tower(4, 'A', 'B', 'C');
	return 0;
}