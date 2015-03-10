#include<stdio.h>
#include<stdlib.h>

int main(int argc, char * argv[]) {
  int i;
  for(i = 0; i<argc; i++) {
    printf("argument %d és %s\n",i , argv[i]);
  }
  return EXIT_SUCCESS;
}
