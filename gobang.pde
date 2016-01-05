int r = 35;
int p[][] = new int[16][16];
ArrayList<Piece> pieces;
int count = 0;
int result;

void setup() {
	size(640, 640);
	frameRate(5);
	textSize(100);
	pieces = new ArrayList<Piece>();
	strokeWeight(2);
	stroke(80);
	for (int i = 1; i < 16; i++) {
		line(40, i * 40, height - 40, i * 40);
		line(i * 40, 40, i * 40, width - 40);
	}
	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 15; j++) {
			p[i][j] = 0;
		}
	}
	stroke(0);
}

void draw() {
	
}

void mousePressed() {
	if (mouseX < 620 && pmouseY < 620) {
		if (count % 2 == 0) {
			pieces.add(new Piece(mouseX, mouseY, 0));
			if (check(mouseX, mouseY, 0) == 1){
				fill(255, 0, 0);
				text("White Win", 60, 300);
				stop();
			}
		}
		else {
			pieces.add(new Piece(mouseX, mouseY, 1));
			if (check(mouseX, mouseY, 1) == 2){
				fill(255, 0, 0);
				text("Black Win", 60, 300);
				stop();
			}
		}
		count++;
	}
}

class Piece {
	int x;
	int y;
	int att;

	Piece (int x, int y, int att) {
		this.x = (x - 20) / 40 + 1;
		this.y = (y - 20) / 40 + 1;
		this.att = att;
		if (p[this.x][this.y] == 0) {
			this.add();
			this.show();
		}
	}

	void add() {
		if (this.att == 0) {
			p[this.x][this.y] = 1;
		}
		else if (this.att == 1) {
			p[this.x][this.y] = -1;
		}
	}

	void show() {
		if (this.att == 0) {
			fill(255);
			ellipse(this.x * 40, this.y * 40, r, r);
		}
		else if (this.att == 1) {
			fill(0);
			ellipse(this.x * 40, this.y * 40, r, r);	
		}
	}

}

int check(int mx, int my, int att) {
	int x = (mx - 20) / 40 + 1;
	int y = (my - 20) / 40 + 1;
	int sx1, sx2, sy1, sy2;
	sx1 = sx2 = sy1 = sy2 = 0;
	int sum;
	if (x == y || x + y == 16) {
	} else {
		if (x < y) {
			sx1 = 1; sy1 = y - x + 1;
			if (x + y < 15) {
				sx2 = 1; sy2 = y + x - 1;
			}
			else if (x + y > 15) {
				sx2 = x - (15 - y); sy2 = 15;
			}
		} else {
			sx1 = x - y + 1; sy1 = 1;
			if (x + y < 15) {
				sx2 = 1; sy2 = y + x - 1;
			}
			else if (x + y > 15) {
				sx2 = x - (15 - y); sy2 = 15;
			}
		}
	}
	for (int i = 0; i < 12; i++) {
		sum = p[x][i] + p[x][i + 1] + p[x][i + 2] + p[x][i + 3] + p[x][i + 4];
		println(sum);
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
		sum = p[i][y] + p[i + 1][y] + p[i + 2][y] + p[i + 3][y] + p[i + 4][y];
		println(sum);
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
	}
	for (int i = 1; i < 12; ++i) {
		sum = p[i][i] + p[i + 1][i + 1] + p[i + 2][i + 2] + p[i + 3][i + 3] + p[i + 4][i + 4];
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
		sum = p[16 - i][i] + p[15 - i][i + 1] + p[14 - i][i + 2] + p[13 - i][i + 3] + p[12 - i][i + 4];
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
	}
	while (sx1 < 12 && sy1 < 12) {
		sum = p[sx1][sy1] + p[sx1 + 1][sy1 + 1] + p[sx1 + 2][sy1 + 2] + p[sx1 + 3][sy1 + 3] + p[sx1 + 4][sy1 + 4];
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
		sx1++;
		sy1++;
	}
	while (sx2 < 12 && sy2 > 4) {
		sum = p[sx2][sy2] + p[sx2 + 1][sy2 - 1] + p[sx2 + 2][sy2 - 2] + p[sx2 + 3][sy2 - 3] + p[sx2 + 4][sy2 - 4];
		if(sum == 5) {
			return 1;
		} else if (sum == -5) {
			return 2;
		}
		sx2++;
		sy2--;
	}
	return 0;
}