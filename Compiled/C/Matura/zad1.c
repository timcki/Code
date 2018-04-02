#include <stdio.h>
#include <stdlib.h>



int
main()
{
	FILE *fp;
	char *line = NULL;
	size_t len = 0;

	int *pixels;
	int i = 0;

	pixels = (int *) malloc(64000 * sizeof(int));
	printf("%p\n", pixels);

	fp = fopen("/home/ft3/Downloads/Dane_PR2/test.txt", "r");
	if (fp == NULL)
		exit(EXIT_FAILURE);

	while (getline(&line, &len, fp) != -1) {
		for (int j = 0; j < 5; j++) {
			sscanf(line, "%d ", &pixels[i++]);
		}
	}

	for (int y = 0; y < 10; y++)
		printf("%d\n", pixels[y]);

	fclose(fp);
	if (line)
		free(line);

	free(pixels);
	return 0;
}

