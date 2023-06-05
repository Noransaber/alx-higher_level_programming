#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @head: ptr to the list head
 * Return: 1 if it has a cycle, 0 if it doesn't
 **/

int check_cycle(listint_t *head)
{
	listint_t *s_ptr = head;
	listint_t *f_ptr = head;

	if (!head)
		return (0);

	while (s_ptr && f_ptr && f_ptr->next)
	{
		s_ptr = s_ptr->next;
		f_ptr = f_ptr->next->next;
		if (s_ptr == f_ptr)
			return (1);
	}
	return (0);
}


