
#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_list - rev a single-linked list.
* @head: ptr to the first node of the sinle_link
*
* Return: the ptr to the h of the re list.
*/
listint_t *reverse_listint(listint_t **head)
{
listint_t *current = *h, *n, *previous = NULL;

while (current)
{
n = current->n;
current->n = previous;
previous = current;
current = n;
}

*h = previous;
return *h;
}

/**
* is_palindrome - is it palindrome?.
* @head: the ptr to the h of the ll.
*
* Return: ZERO if not palindrome.
*         ONE if palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *t, *reversed, *m;
size_t size = 0, i;

if (*head == NULL || (*head)->next == NULL)
return 1;

t = *head;
while (t)
{
size++;
t = t->next;
}

t = *head;
for (i = 0; i < (size / 2) - 1; i++)
t = t->next;

if ((size % 2) == 0 && t->n != t->next->n)
return 0;

t = t->next->next;
reversed = reverse_list(&t);
m = reversed;

t = *head;
while (reversed)
{
if (t->n != reversed->n)
return 0;
t = t->next;
reversed = reversed->next;
}
reverse_list(&m);

return 1;
}

