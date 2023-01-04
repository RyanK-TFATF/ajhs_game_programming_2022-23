// Loops, Ryan Kelley, v0.3a
using System;

namespace _03_Loops
{
    class Program
    {
        static void Main(string[] args)
        {
            /* while loop -- best used if you DO NOT know how many iterations needed
            // Control Variable -- Used to determine when to start/stop loop. 
            int loopCounter = 0; 
            while (loopCounter <= 100) // Loop ONLY runs if this line is TRUE. 
            {
                Console.WriteLine(loopCounter);
                loopCounter++;
            }
            
            // do/while loop -- do block is ALWAYS executed once, then use conditional
            int i = 0; 
            do 
            {
                i++;
                Console.WriteLine(i);    
            }
            while (i < 1); 
            */ 

            // for loop -- When you know how many iterations are needed.  
            // STATEMENT 1 -- EXECUTED ONE TIME BEFORE LOOP STARTS. 
            // STATEMENT 2 -- CONDITIONAL STATEMENT TO DETERMINE IF LOOP EXECUTES
            // STATEMENT 3 -- CODE EXECUTES AFTER EACH ITERATION OF THE LOOP. 
            /* 
            for (statement1; statement2; statement3) 
            {
            doCodeStuffHere; 
            }
            
            for (int i = 0; i < 100; i++)
            {
                Console.WriteLine(i);
                if (i % 2 == 0) {
                    Console.WriteLine("That number is even.\n");
                } else {
                    Console.WriteLine("That number is odd.\n");
                }
            }
            */

            // Nested For Loops 
            // Outer Loop 
            for (int i = 0; i < 1000; i++) 
            {
                Console.WriteLine("Outer Loop Counter:" + i);
                // Inner Loop 
                for (int j = 1; j < 500; j++)
                {
                    Console.WriteLine("Inner Loop Counter:" + j);
                }
            }

        }
    }
}
