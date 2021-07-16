public class Queue{
    int queue[];
    int size;
    int front;
    int rear;
    public Queue(int n){
        queue=new int[5];
        enqueue(n);
    }

    public void enqueue(int data){
        if(!isFull()){
        queue[rear]=data;
        rear=(rear+1)%5;
        size=size+1;
        }
        else{
            System.out.println("queue if Full");
        }

    }
    public int dequeue()
    {
      int data=queue[front];
      if(!isEmpty()){
      front=(front+1)%5;
      size=size-1;
      }
      else{
          System.out.println("queue is Empty");
      }
      return data;
    }
      public int peek()
      {
        int data=queue[front];
        return data;


    }
    public void show(){
        System.out.print("Elements: ");
        for(int i=0;i<size;i++){
            System.out.print(queue[(front+i)%5]+" ");
        }
        System.out.println();
        for(int n: queue){
            System.out.print(n +" ");
        }
    }
    public int getsize(){
        return size;
    }
    public boolean isEmpty(){
        return size==0;
    }
    public boolean isFull(){
        return size==5;
    }

   /*public static void main(String[] args){
        Queue q=new Queue(5);
        q.enqueue(5);
        q.enqueue(2);
        q.enqueue(7);
        q.enqueue(3);
       
        q.dequeue();
        q.dequeue();
       
        q.enqueue(1);
        q.enqueue(9);

        System.out.println(q.isEmpty());
        System.out.println(q.isFull());
        
        System.out.println("size"+q.getsize());
        q.show();

    }*/
}