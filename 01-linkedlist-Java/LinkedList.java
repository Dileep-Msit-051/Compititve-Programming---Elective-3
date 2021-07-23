
class Element{
	int value;
	Element next;
	public Element(int value){
		this.value = value;
		this.next = null;
	}
}

public class LinkedList{
	Element head;
	public LinkedList(Element head){
		this.head = head;
	}
 public void display() {
        LinkedList current = head;
        while (current != null) {
            System.out.print(current.value + "-- ");
            current = current.next;
        }
        System.out.print("null");
    }

 public int length() {
        if (head == null) {
            return 0;
        }
        int count = 0;
        Element current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

public void append(Element new_element){
		LinkedList newnode= new LinkedList(new_element);
		newnode.next=head;
		head=newnode;

	}

	public Element get_position(int position){
		// Get an element from a particular position.
        // Assume the first position is "1".
        // Return null if position is not in the list
		// Your code goes here
		return null;
	}

	public void insert(Element new_element, int position){
	   // """Insert a new node at the given position.
       // Assume the first position is "1".
       // Inserting at position 3 means between
       // the 2nd and 3rd elements."""
		// Your code goes here

	}

	public void delete(int value){
		// Delete the first node with a given value.
		// Your code goes here
	}
}
