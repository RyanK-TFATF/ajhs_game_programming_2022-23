// Summation Calculator, Ryan Kelley, v0.0a 
using System;

namespace _01_SummationCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0 
            int lowerLimit = 0;
            int upperLimit = 0; 
            Console.WriteLine("What is the lower limit for the summation?");
            lowerLimit = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("What is the upper limit for the summation?");
            upperLimit = Convert.ToInt32(Console.ReadLine());
            for (n = lowerLimit; n <= upperLimit; n++)
            {
                sum += (n * n) / (3 * n); // Update this line to reflect the equation for which you are solving. 
                Console.WriteLine(sum);
            }
                            
        }
    }
}
