// Ryan Kelley, Program Template, v0.01
using System; 

namespace Operators
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create TWO String, Integer, and Float variables.
            string myString1 = "I like potato salad."            ;
            string myString2 = "Sometimes I like to run in the rain.";

            int myInt1 = 9001;
            int myInt2 = -5;

            float myFloat1 = 0.0F;
            float myFloat2 = -1.25F;

            // Arithmetic Operators 
            Console.WriteLine(myInt1 + myInt2);
            Console.WriteLine(myString1 + myString2);
            Console.WriteLine(myFloat1 + myFloat2);
            Console.WriteLine(myInt1 + myFloat2); 

            Console.WriteLine(myInt1 - myInt2);
            //Console.WriteLine(myString1 - myString2);
            Console.WriteLine(myFloat1 - myFloat2);
            Console.WriteLine(myInt1 - myFloat2); 

            Console.WriteLine(myInt1 / myInt2);
            //Console.WriteLine(myString1 / myString2);
            Console.WriteLine(myFloat1 / myFloat2);
            Console.WriteLine(myInt1 / myFloat2); 

            Console.WriteLine(myInt1 * myInt2);
            //Console.WriteLine(myString1 * myString2);
            Console.WriteLine(myFloat1 * myFloat2);
            Console.WriteLine(myInt1 * myFloat2); 

            // Modulus 
            Console.WriteLine("Modulus");
            Console.WriteLine(10 % 2); 
            Console.WriteLine(9 % 4); 
            
            // Increment
            int myInt3 = 1;
            myInt2++; 
            Console.WriteLine(myInt3);

            // Decrement 
            int myInt4 = 2;
            myInt3--; 
            Console.WriteLine(myInt4);

            // Assignment Operators 
            // =
            // +=
            // -=
            // *= 
            // /= 

            // Comparison Operators 
            // Is Equal To 
            // Greater Than
            // Greater Than or Equal To 
            // Less Than
            // Less Than or Equal To 
            // Not Equal To 

            // Logical Operators
            // And
            // Or
            // Not 

        }
    }
}
