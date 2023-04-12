// Summation Calculator, YOUR_NAME_HERE, v0.0a 
using System;

namespace _01_SummationCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            int lowerLimit = 0;
            int upperLimit = 0; 
            Console.WriteLine("What is the lower limit?");
            lowerLimit = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("What is the upper limit?");
            upperLimit = Convert.ToInt32(Console.ReadLine());
            for (int n = lowerLimit; n <= upperLimit; n++)
            {
                sum += n * n;
                Console.WriteLine(sum);
            }                            
        }
    }
}
