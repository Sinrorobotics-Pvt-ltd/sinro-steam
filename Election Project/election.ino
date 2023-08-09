#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define VOTE_BUTTON_PIN 2
#define RESULT_BUTTON_PIN 3

#define NUM_CANDIDATES 7

int candidatePins[NUM_CANDIDATES] = {4, 5, 6, 7, 8, 9, 10}; // Pins for each candidate
int votes[NUM_CANDIDATES] = {0};

void setup() {
  pinMode(VOTE_BUTTON_PIN, INPUT_PULLUP);
  pinMode(RESULT_BUTTON_PIN, INPUT_PULLUP);

  for (int i = 0; i < NUM_CANDIDATES; i++) {
    pinMode(candidatePins[i], INPUT_PULLUP);
  }

  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Voting Machine");
  display.display();
}

void loop() {
  if (digitalRead(VOTE_BUTTON_PIN) == LOW) {
    int selectedCandidate = getSelectedCandidate();
    if (selectedCandidate >= 0 && selectedCandidate < NUM_CANDIDATES) {
      votes[selectedCandidate]++;
      display.clearDisplay();
      display.setCursor(0, 0);
      display.print("Vote for Candidate ");
      display.println(selectedCandidate + 1);
      display.display();
      delay(1000);
    }
  }

  if (digitalRead(RESULT_BUTTON_PIN) == LOW) {
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println("Election Results:");
    for (int i = 0; i < NUM_CANDIDATES; i++) {
      display.print("Candidate ");
      display.print(i + 1);
      display.print(": ");
      display.println(votes[i]);
    }
    display.display();
    while (digitalRead(RESULT_BUTTON_PIN) == LOW) {
      // Wait for button release
    }
  }
}

int getSelectedCandidate() {
  for (int i = 0; i < NUM_CANDIDATES; i++) {
    if (digitalRead(candidatePins[i]) == LOW) {
      return i;
    }
  }
  return -1; // No candidate selected
}


//  SINRO ELECTION