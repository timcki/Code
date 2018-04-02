
/* PART 1
* Memory is allocated in a spiral so we establish the algorithm. It goes like this:
    * 1 Right
    * 1 Up
    * 2 Left
    * 2 Down
    * 3 Right
    * 3 Up
    * 4 Left
    * etc..
 * so we code that to 
 * PART 2
 * Memory is still alocated in a spiral but this time it's just dumb af. Making an array to hold my "memory" and then 
 * adding elements till it works
 */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int calc_result(int x, int y);
int part_1();
int part_2();

int num = 289326;

int main() {
    	part_2();
    	printf("RESULT: %d", part_1());
        return 0;
}

int calc_result(int x, int y) {
    return abs(x) + abs(y);
}

int part_2() {
    static int memory[31][31];
	int x = 16; int y = 16;
	int count = 1;
	for (int i=0; i<31; i++) { for (int j=0; j<31; j++) printf("%d ", memory[i][j]); printf("\n"); }
	memory[x][y] = 1;
	while (1) {
		//if (count % 2) {
    		//for (int i=0; i<count; i++) {
        		//x+=1;
        		//test

	return 0;
    		}
}

int part_1() {
	int x = 0; int y = 0;
    int test = 1; int count = 1;
    while (1) {
        if (count % 2) {
            for (int i=0; i<count; i++) {
                x += 1;
                test += 1;
                if (test == num) return calc_result(x, y);
            }
            for (int i=0; i<count; i++) {
                y += 1;
                test += 1;
                if (test == num) return calc_result(x, y);
            }
        }
        else {
            for (int i=0; i<count; i++) {
                x -= 1;
                test += 1;
                if (test == num) return calc_result(x, y);
            }
            for (int i=0; i<count; i++) {
                y -= 1;
                test += 1;
                if (test == num) return calc_result(x, y);
            }
        }
        count++;
    }
}
