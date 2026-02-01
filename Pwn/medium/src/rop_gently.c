#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


void ignore_me() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void vulnerable() {
    char buffer[40];
    puts("Can you ROP your way out of this?");
    read(0, buffer, 0x100);
}

int main() {
    ignore_me();
    vulnerable();
    return 0;
}
