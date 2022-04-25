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
	listint_t *current, *tmp;

    current = list;
    tmp = current->next;
    while (current != NULL)
    {
	    current = current->next;

	    if (current == list || current == tmp)
		    return (1);
    }

    return (0);
}
