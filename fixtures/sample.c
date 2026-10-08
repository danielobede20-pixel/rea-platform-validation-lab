#include <stdio.h>
static int classify_lead(int orders, int high_interest) {
    if (orders >= 3) return 100;
    if (high_interest) return 50;
    return 10;
}
int main(void) {
    int score = classify_lead(4, 1);
    printf("fixture-score=%d\n", score);
    return score == 100 ? 0 : 1;
}
