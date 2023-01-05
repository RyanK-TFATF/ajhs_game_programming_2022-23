// 03_Loops, Ryan Kelley, v0.2a
using System;

namespace _03_Loops
{
    class Program
    {
        static void Main(string[] args)
        {
           /* while loop -- best used when you do not know number of iterations
           int loopCounter = 0; 
           while (loopCounter < 1000)
           {
            // Continue the loop. 
            if (loopCounter == 256)
            {
                loopCounter++;
                continue; 
            }
            Console.WriteLine("Loop Counter:" + loopCounter); 
            loopCounter++; 
             Break from loop. 
            if (loopCounter == 750)
            {
                break; // STOP THE LOOP! 
            }
            */ 
            
            /* do/while loop 
            int i = 0; 
            do 
            {
                Console.WriteLine("Loop Counter:" + i); 
                i++; 
            }
            while (i < 1);
            do block ALWAYS RUNS ONE TIME, then runs based on while condition. 
            */

            // for loops 
            // STATEMENT 1 -- executes ONCE before the loop starts. 
            // STATEMENT 2 -- CONDITIONAL statement, checked each time after 1st loop
            // STATEMENT 3 -- executes EVERY TIME after loop completes 
            // for (statement1; statement2; statement3)
            for (int i = 0; i <= 250; i++)
            {
                Console.WriteLine(i);
                if (i % 2 == 0)
                {
                    Console.WriteLine("This number is even.");
                } else {
                    Console.WriteLine("This number is odd."); 
                }
            }

            

           


        }
    }
}
