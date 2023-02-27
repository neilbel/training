/*
  Neil Belh Hadj
  La factorielle récursive et itérative en C.
  Pour compiler : gcc fact.c -o fact
  Puis : ./fact
 */
#include <stdio.h>

int fact_r(int n) {
  if(n<2)
    return 1;
  else
    return n * fact_r(n-1);
}


int fact_i(int n) {
  int p = 1, i;
  for(i = 2;i <= n;i++)
    p *= i;
  return p;
}


int main() {
  printf("5! --->>> %d (récursive)\n", fact_r(5));
  printf("6! --->>> %d (itérative)\n", fact_i(6));
  return 0;
}
