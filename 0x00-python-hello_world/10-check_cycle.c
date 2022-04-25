#include "lists.h"

/**
 * check_cycle - check the code
 * @list: ...
 *
 * Return: 1 Success
 * Otherwise 0
 */
int check_cycle(listint_t *list)
{
    listint_t *current;

    current = list;
    while (current != NULL)
    {
	    current = current->next;

	    if (current == list)
		    return (1);
    }

    return (0);
}
