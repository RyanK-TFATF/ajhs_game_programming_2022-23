// Ryan Kelley, Program Template, v0.01
using System; 
/*
Void Method
Method with Return
Method with Parameter
Method with Multiple Parameters
Method with Default Parameters
Method Class using Named Arguments
Method Overloading 
*/
namespace MethodsParameters 
{
    class MethodsParameters
    {
        // METHOD -- named block of code, can be used over and over. 
        // All methods have a SIGNATURE that defines their name, parameters, and output.
        // Example Signature 
        static void MyMethod() 
        {
            Console.WriteLine("I like mine with lettuce and tomatoes, Heinz 57, and french fried potatoes.\n");
        }
        // static -- This method belongs to the current class, it is NOT an object. 
        // void -- This method has no return value. 

        static int DoubleUp()
        {
            int sum = 0; 
            Console.WriteLine("This method will double a number and return it.\n");
            Console.WriteLine("Please enter a number on the next line.\n");
            sum = System.Convert.ToInt32(Console.ReadLine());            
            sum *= 2;   
            Console.WriteLine(sum);          
            return sum; 
        }

        // Methods with Parameters  
        static void MakePancakes(int num)
        {
            for (int i = 0; i < num; i++) 
            {
                Console.WriteLine("One golden, fluffy pancake coming up!\n");
            }
        }

        static void MakeEggs(int num, string style)
        {
            Console.WriteLine("You have ordered" + num + "eggs cooked " + style + ".\n");
        }

        // Using Defaults for Parameters
        static void MakeBurger(int num = 1)
        {
            Console.WriteLine("I am going to cook " + num + "hamburgers.\n");
        }

        // Named Arguments 
        static void AllMyChildren(string child1, string child2, string child3)
        {
            Console.WriteLine("My favorite child is " + child3);
        }

        // METHOD OVERLOADING 
        // Find Sum of Int 
        static int FindSum(int x, int y)
        {
            int sum = x + y; 
            Console.WriteLine("Sum: " + sum); 
            return sum; 
        }
        
        // Find Sum of Double 
        static double FindSum(double x, double y)
        {
            double sum = x + y; 
            Console.WriteLine("Sum: " + sum); 
            return sum; 
        }

        static void Main(string[] args)
        {
            //MyMethod();    
            //DoubleUp(); 
            //MakePancakes(); 
            //MakeEggs(10, "sunny side up"); 
            //MakeBurger(); 
            //MakeBurger(10); 
            //AllMyChildren(child3: "Steve", child2: "Susan", child1: "Chewbacca");
            FindSum(1, 5); // TWO INTEGERS
            FindSum(9.5, 2.4); // TWO DOUBLES
            FindSum(5, 2.5);  // ONE OF EACH 
        }
    }
}
