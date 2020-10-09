#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char**argv)
{
  int retval;
  int status;
  int pchild = fork();

  if (-1 == pchild)
  { // Erreur au fork
    fprintf(stderr, "ERREUR AU FORK\n");
    exit(-1);
  }

  if (0 == pchild)
  { // code du fils
    printf("CHILD : Enter an exit value : ");
    scanf("%d", &retval);
    sleep(1);
    exit(retval);
  }
  else
  { // code du père
    printf("PARENT : JE SUIS TON PERE et tu as le PID %d\n", pchild);
    wait(&status);
    printf("PARENT : Child has terminated with exit code %d\n",

    WEXITSTATUS(status));
    exit(0);
  }
}
