#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Compiler flags: gcc -fno-stack-protector -no-pie -o hello_overflow hello_overflow.c

void ignore_me() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
    ignore_me();
    
    int secret = 0x12345678;
    char buffer[32];

    printf("Hello! Can you overflow me?\n");
    printf("Current secret: 0x%x\n", secret);
    printf("Give me some input: ");
    
    // Vulnerability: read allows reading more than 32 bytes
    read(0, buffer, 0x100);

    if (secret == 0xdeadbeef) {
        printf("\nWow! You changed the secret!\n");
        printf("Here is your flag:\n");
        system("cat flag.txt");
    } else {
        printf("\nNah, secret is still 0x%x. Try again!\n", secret);
    }

    return 0;
}
