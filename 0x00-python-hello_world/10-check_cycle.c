#include "lists.h"

/**
 * check_cycle - checks if list contains cycle in it
 * @list: singly linked list
 * Return: 1 if true 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr = list;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
