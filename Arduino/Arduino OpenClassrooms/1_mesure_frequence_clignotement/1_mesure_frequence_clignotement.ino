const int CONNEXION = 13;
unsigned long tempsFin;
unsigned long  tempsDepart;

void setup()
{
  Serial.begin(9600);
  pinMode(CONNEXION,OUTPUT);
}

void loop()
{
  tempsDepart = micros();
  digitalWrite(CONNEXION,HIGH);
  delay (1000);
  digitalWrite(CONNEXION,LOW);
  delay (1000);
  tempsFin = micros();
  Serial.println(tempsFin-tempsDepart);
}
