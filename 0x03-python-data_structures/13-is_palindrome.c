#include "lists.h"

/**
 * is_palindrome - test if the linked lists is palindrome
 * @head: address of pointers to lists
 * Return: 1 is palindromes else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *node, *prev;
	int failed = 0;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	node = slow;
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	fast = *head;
	node = prev;
	while (prev)
	{
		if (fast->n != prev->n)
		{
			failed = 1;
			break;
		}
		fast = fast->next;
		prev = prev->next;
	}
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	return (!failed);
}