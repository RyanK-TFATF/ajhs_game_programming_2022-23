// Arrays and ArrayLists, Ryan Kelley, 11/06/22, 11:24PM, v0.0 
using System;

namespace ListsArrays
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaring Arrays -- Method 0 -- Creating Empty Array
            // dataType[] arrayName;
            // Values can be added later. 

            // Declaring Arrays -- Method 1 -- Creating Array with Values
            // dataType[] arrayName = {value0, value1, value2, ...};
            // Values can be changed later. 

            // Declaring Arrays -- Method 2 -- Create Array and Specify Size 
            // dataType[] arrayName = new dataType[numElements];

            // Declare and Define Three Arrays -- string, integer, and float or double v0.1
            string[] breakfastFoods = {"Bacon", "Waffles", "Pancakes", "Cereal", "Parfait"};
            int[] testScores = {95, 100, 25, 15, 27, 35};
            float[] GPA = {3.14f, 2.25f, 1.74f, 1.99f, 0.99f, 4.25f};
            
            // Print First Element v0.2a
            Console.WriteLine(breakfastFoods[0]);
            Console.WriteLine(testScores[0]);
            Console.WriteLine(GPA[0]);

            // Print First Element v0.2b
            

            // Print Array Length v0.3 
            Console.WriteLine(breakfastFoods.Length);
            Console.WriteLine(testScores.Length);
            Console.WriteLine(GPA.Length);
        }
    }
}
