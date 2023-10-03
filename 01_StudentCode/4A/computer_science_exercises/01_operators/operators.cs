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
            // =  THIS ASSIGNMET OPERATOR THROWS OUT OLD VALUES
            myInt3 = 5; 
            // These assignment operators keep old values!!             
            // +=
            myInt3 += -1;
            // -=
            myInt3 -= 2;
            // *= 
            myInt3 *= 3;            
            // /= 
            myInt3 /= 2; 
            Console.WriteLine(myInt3); 

            // Comparison Operators 
            // Is Equal To 
            Console.WriteLine(5 == 4); 
            // Not Equal To 
            Console.WriteLine(3 != 2);
            // Greater Than
            Console.WriteLine(5 > 3);
            // Greater Than or Equal To 
            Console.WriteLine(55 >= 75); 
            // Less Than
            Console.WriteLine(-1 < -2);
            // Less Than or Equal To 
            Console.WriteLine(1 <= 5); 
            

            // Logical Operators
            // And -- ALL CONDITIONS MUST BE TRUE FOR WHOLE STATEMENT TRUE
            Console.WriteLine(3 > 2 && 2 == 2); // True and True = True
            Console.WriteLine(3 > 2 && 5 > 6); // True and False = False
            // Or -- ONE condition must be true for the whole statement to be true. 
            Console.WriteLine(5 < 9 || 5 != 4); // True or True == True
            Console.WriteLine(9 < 10 || 3 > 5); // True or False == True
            // Not -- Find the 'opposite' value. 
            Console.WriteLine(!True); // 

        }
    }
}
