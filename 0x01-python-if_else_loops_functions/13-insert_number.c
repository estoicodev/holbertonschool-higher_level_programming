#include "lists.h"

/**
 * create_nodeint - Create a new node listint_t
 * @n: Integer
 *
 * Return: void
 */
listint_t *create_nodeint(int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;

	return (new);
}

/**
 * insert_node -  Inserts a number into a sorted singly linked list.
 * @head: The pointer of the pointer of the head element of the singled list
 * @number: Integer of the new node
 *
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = create_nodeint(number);
	listint_t *tmp = *head;
	int flag = 0;

	if (new == NULL || head == NULL || *head == NULL)
		return (NULL);

	if (new->n <= tmp->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (tmp->next != NULL)
	{
		if (new->n <= tmp->next->n)
		{
			flag = 1;
			break;
		}
		tmp = tmp->next;
	}

	if (flag == 1)
		new->next = tmp->next;

	tmp->next = new;

	return (new);
}
