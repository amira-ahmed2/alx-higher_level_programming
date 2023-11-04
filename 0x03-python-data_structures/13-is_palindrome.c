#include "lists.h"

#include <stdio.h>
#include <stdlib.h>

// تعريف هيكل العقدة في القائمة المتصلة
struct listint_t {
    int n;
    struct listint_t *next;
};

// دالة لعكس القائمة المتصلة
struct listint_t *reverseList(struct listint_t *head) {
    struct listint_t *prev = NULL;
    struct listint_t *current = head;
    struct listint_t *next = NULL;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    return prev;
}

// دالة للتحقق مما إذا كانت القائمة متصلة باليندروم أم لا
int is_palindrome(struct listint_t **head) {
    // التحقق من حالات القوائم الفارغة أو القوائم التي تحتوي على عقدة واحدة
    if (*head == NULL || (*head)->next == NULL) {
        return 1; // قائمة فارغة أو تحتوي على عقدة واحدة وتعتبر باليندروم
    }
    
    struct listint_t *slow = *head;
    struct listint_t *fast = *head;
    struct listint_t *prev_slow = *head;
    struct listint_t *mid = NULL;
    int isPalindrome = 1;

    // استخدام الفهرسين البطيء والسريع للعثور على منتصف القائمة
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // إذا كان لديك عدد زوجي من العقد، ستكون "slow" في منتصف القائمة
    // إذا كان لديك عدد فردي من العقد، ستكون "slow" في العقدة الوسطى
    // سيتم استخدام "mid" للإشارة إلى العقدة الوسطى إذا كان العدد فرديًا
    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    // عكس الجزء الثاني من القائمة
    struct listint_t *second_half = reverseList(slow);

    // مقارنة الجزء الأول والجزء الثاني المعكوس
    struct listint_t *first_half = *head;
    while (second_half != NULL) {
        if (first_half->n != second_half->n) {
            isPalindrome = 0; // القائمة ليست باليندروم
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // استعادة القائمة الأصلية بعد المقارنة
    second_half = reverseList(second_half);

    // إذا كان هناك عقدة وسطية، سنربطها مرة أخرى بالقائمة
    if (mid != NULL) {
        prev_slow->next = mid;
        mid->next = second_half;
    } else {
        prev_slow->next = second_half;
    }

    return isPalindrome;
}

