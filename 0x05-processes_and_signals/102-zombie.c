#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * infinite_while - loop forever, doing nothing
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry point, creates 5 zombie processes
 *
 * Return: 0 if the infinite loop exits
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 1)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
