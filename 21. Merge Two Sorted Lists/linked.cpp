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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *result = NULL;

        // to point to thr last result pointer
        ListNode **lastPtrRef = &result;

        while (1)
        {
            if (l1 == NULL)
            {
                *lastPtrRef = l2;
                break;
            }

            else if (l2 == NULL)
            {
                *lastPtrRef = l1;
                break;
            }

            if (l1->val <= l2->val)
                MoveNode(lastPtrRef, &l1);

            else
                MoveNode(lastPtrRef, &l2);

            // advance to point to the next '.next' field
            lastPtrRef = &((*lastPtrRef)->next);
        }
        return (result);
    }

    void MoveNode(ListNode **destRef, ListNode **sourceRef)
    {
        // the front source node 
        ListNode *newNode = *sourceRef;
        assert(newNode != NULL);

        // Advance the source pointer 
        *sourceRef = newNode->next;

        // Link the old dest off the new node 
        newNode->next = *destRef;

        // Move dest to point to the new node 
        *destRef = newNode;
    }
};