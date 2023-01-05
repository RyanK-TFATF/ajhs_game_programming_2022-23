// 03_Loops, Ryan Kelley, v0.1c
using System;

namespace _03_Loops
{
    class Program
    {
        static void Main(string[] args)
        {
           // while loop -- best used when you do not know number of iterations
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
            /* Break from loop. 
            if (loopCounter == 750)
            {
                break; // STOP THE LOOP! 
            }
            */ 
            

           }


        }
    }
}
