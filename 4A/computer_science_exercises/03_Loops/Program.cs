// Loops, Ryan Kelley, v0.1a
using System;

namespace _03_Loops
{
    class Program
    {
        static void Main(string[] args)
        {
            // while loop -- best used if you DO NOT know how many iterations needed
            // Control Variable -- Used to determine when to start/stop loop. 
            int loopCounter = 0; 
            while (loopCounter <= 100) 
            {
                Console.WriteLine(loopCounter);
                loopCounter++;
            }
        }
    }
}
