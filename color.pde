PGraphics mod;
/*
PImage mod;
void settings() {
	mod = loadImage("mod.jpg");
	size(mod.width, mod.height);
}
*/
void setup(){
	size(512, 512);
	background(255);
	mod = createGraphics(width, height);
	smooth();
	noLoop();
}

void draw(){
	mod.beginDraw();
	mod.background(255);
	mod.background(255);
	mod.noFill();
	mod.strokeWeight(10);
	mod.ellipse(width/2, height/2, 400, 400);
	mod.endDraw();
	//image(mod, 0, 0);
	mod.loadPixels();
	mod.filter(BLUR);
	colorMode(HSB);
	for(int x=0;x<mod.width;x+=1){
		for(int y=0;y<mod.height;y+=1){
			int loc=x+y*mod.width;
			if(brightness(mod.pixels[loc]) < 200){
				float c=map(x,0,mod.width,0,255);
				stroke(c, 255, 255);
				point(x, y);
			}
		}
	}
}