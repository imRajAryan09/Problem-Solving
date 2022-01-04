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
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *temp = head;

        // traverse further only if there are at - least two nodes left
        while (temp != NULL && temp->next != NULL)
        {
            // swap data of node with its next node's data
            swap(temp->val, temp->next->val);

            // move temp by 2 for the next pair
            temp = temp->next->next;
        }
        return head;
    }
};