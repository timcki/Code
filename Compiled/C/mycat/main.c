/* Basic implementation of netcat to learn some networking */

#include <stdio.h>
#include <sys/socket.h>

struct sockaddr_in server;

int
main()
{
	int soc;
	soc = socket(AF_INET, SOCK_STREAM, 0);
	if (soc < 0)
		printf("Error creating socket\n");
	return 0;
}
