unsigned int x, y, z;

void setup() {  
	pinMode(A0, INPUT);
	pinMode(A1, INPUT);
	pinMode(A2, INPUT);  
  
	Serial.begin(9600);
}

void loop() { 
	x = analogRead(A0);
	y = analogRead(A1);
	z = analogRead(A2);
  
	Serial.println("xxxx | yyyy | zzzz");
	Serial.print(x, DEC);
	Serial.print(" | ");
	Serial.print(y, DEC);
	Serial.print(" | ");
	Serial.print(z, DEC);
	Serial.println(" | "); 
	delay(2000);
  
}