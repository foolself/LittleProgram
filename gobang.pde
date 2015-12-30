int r = 35;
int pB[][] = new int[16][16];
int pW[][] = new int[16][16];
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
			pB[i][j] = 0;
			pW[i][j] = 0;
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
				text("White Wine", 60, 300);
				stop();
			}
		}
		else {
			pieces.add(new Piece(mouseX, mouseY, 1));
			if (check(mouseX, mouseY, 1) == 2){
				fill(255, 0, 0);
				text("Black Wine", 60, 300);
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
		this.add();
		this.show();
	}

	void add() {
		if (this.att == 0) {
			pW[this.x][this.y] = 1;
		}
		else if (this.att == 1) {
			pB[this.x][this.y] = 1;
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
		println(sx1 + "," + sy1 + "," + sx2 + "," + sy2);
	}
	if (att == 0) {
		for (int i = 0; i < 12; i++) {
			if((pW[x][i] + pW[x][i + 1] + pW[x][i + 2] + pW[x][i + 3] + pW[x][i + 4]) == 5) {
				return 1;
			}
			if ((pW[i][y] + pW[i + 1][y] + pW[i + 2][y] + pW[i + 3][y] + pW[i + 4][y]) == 5) {
				return 1;
			}
		}
		for (int i = 1; i < 12; ++i) {
			if ((pW[i][i] + pW[i + 1][i + 1] + pW[i + 2][i + 2] + pW[i + 3][i + 3] + pW[i + 4][i + 4]) == 5) {
				return 1;
			}
			if ((pW[16 - i][i] + pW[15 - i][i + 1] + pW[14 - i][i + 2] + pW[13 - i][i + 3] + pW[12 - i][i + 4]) == 5) {
				return 1;
			}
		}
		while (sx1 < 12 && sy1 < 12) {
			if ((pW[sx1][sy1] + pW[sx1 + 1][sy1 + 1] + pW[sx1 + 2][sy1 + 2] + pW[sx1 + 3][sy1 + 3] + pW[sx1 + 4][sy1 + 4]) == 5) {
				return 1;	
			}
			sx1++;
			sy1++;
		}
		while (sx2 < 12 && sy2 > 4) {
			if ((pW[sx2][sy2] + pW[sx2 + 1][sy2 - 1] + pW[sx2 + 2][sy2 - 2] + pW[sx2 + 3][sy2 - 3] + pW[sx2 + 4][sy2 - 4]) == 5) {
				return 1;	
			}
			sx2++;
			sy2--;
		}

	}
	if (att == 1) {
		for (int i = 0; i < 10; i++) {
			if((pB[x][i] + pB[x][i + 1] + pB[x][i + 2] + pB[x][i + 3] + pB[x][i + 4]) == 5) {
				return 2;
			}
			if ((pB[i][y] + pB[i + 1][y] + pB[i + 2][y] + pB[i + 3][y] + pB[i + 4][y]) == 5) {
				return 2;
			}
		}
		for (int i = 1; i < 12; ++i) {
			if ((pB[i][i] + pB[i + 1][i + 1] + pB[i + 2][i + 2] + pB[i + 3][i + 3] + pB[i + 4][i + 4]) == 5) {
				return 1;
			}
			if ((pB[16 - i][i] + pB[15 - i][i + 1] + pB[14 - i][i + 2] + pB[13 - i][i + 3] + pB[12 - i][i + 4]) == 5) {
				return 1;
			}
		}
		while (sx1 < 12 && sy1 < 12) {
			if ((pB[sx1][sy1] + pB[sx1 + 1][sy1 + 1] + pB[sx1 + 2][sy1 + 2] + pB[sx1 + 3][sy1 + 3] + pB[sx1 + 4][sy1 + 4]) == 5) {
				return 2;	
			}
			sx1++;
			sy1++;
		}
		while (sx2 < 12 && sy2 > 4) {
			if ((pB[sx2][sy2] + pB[sx2 + 1][sy2 - 1] + pB[sx2 + 2][sy2 - 2] + pB[sx2 + 3][sy2 - 3] + pB[sx2 + 4][sy2 - 4]) == 5) {
				return 2;	
			}
			sx2++;
			sy2--;
		}
	}
	return 0;
}