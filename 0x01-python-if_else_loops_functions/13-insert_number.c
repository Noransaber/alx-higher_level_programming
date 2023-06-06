#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a num is inserted into the list
 * @head: head pte
 * @number: num to be inserted
 *
 * Return: on failer - NULL.
 * Otherwise - new nod ptr.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *n;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->n = number;

	if (node == NULL || node->n >= number)
	{
		n->next = node;
		*head = n;
		return (n);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	n->next = node->next;
	node->next = n;

	return (n);
}
