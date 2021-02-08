#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Waits forever
 *
 * Return: Always 0
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
 * main - Creates 5 zombie processes
 *
 * Return: Always 0
 */

int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
