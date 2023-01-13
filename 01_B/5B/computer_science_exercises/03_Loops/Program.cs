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

            int[] grades = {
                55, 
                75, 
                68,
                15, 
                100, 
                0,
                99, 
                50,
                86, 
                65
            }; 

            foreach (int i in grades) {
                if (i >= 90) {
                    Console.WriteLine(i);
                    Console.WriteLine("This is an A.");
                } else if (i >= 80) {
                    Console.WriteLine(i);
                    Console.WriteLine("This is a B.");
                } else if (i >= 70) {
                    Console.WriteLine(i);
                    Console.WriteLine("This is a C.");
                } else if (i >= 60) {
                    Console.WriteLine(i);
                    Console.WriteLine("This is a D.");
                } else if (i >= 0) {
                    Console.WriteLine(i);
                    Console.WriteLine("This is a F.");
                } else {
                    Console.WriteLine("Error calculating grade.  Please verify data.");
                }
            }

            

           


        }
    }
}
