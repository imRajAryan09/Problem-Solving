#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for singly-linked list.
 * */

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        // to store the length of the linked list
        int len = 0;
        ListNode *tmp = head;

        while (tmp != NULL)
        {
            len++;
            tmp = tmp->next;
        }

        if (n == len)
            return head->next;

        else
        {
            // remove len-n th node from starting
            int diff = len - n;
            ListNode *prev = NULL;
            ListNode *curr = head;

            for(int i=0;i<diff;i++)
            {
                prev=curr;
                curr=curr->next;
            }
            prev->next=curr->next;
            return head;
        }
    }
};