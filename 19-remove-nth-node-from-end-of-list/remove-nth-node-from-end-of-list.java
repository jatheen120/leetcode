class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode d=new ListNode(0);
        d.next=head;

        ListNode one=d;
        ListNode two=d;

        for (int i=0;i<n;i++){
            one=one.next;
        }
        while(one.next!=null) {
            one=one.next;
            two=two.next;
        }
        two.next=two.next.next;
        return d.next;
    }
}
