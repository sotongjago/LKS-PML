#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc -fno-stack-protector -no-pie -o ret2win ret2win.c

void ignore_me() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void win() {
    printf("Congratulations! You redirected execution here!\n");
    system("cat flag.txt");
    exit(0);
}

void vulnerable() {
    char buffer[64];
    printf("Try to redirect me to win() function!\n");
    printf("Input: ");
    read(0, buffer, 0x100);
}

int main() {
    ignore_me();
    vulnerable();
    return 0;
}
