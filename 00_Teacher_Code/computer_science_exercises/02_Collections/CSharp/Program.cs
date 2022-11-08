using System;

namespace _02_Collections
{
    class Program
    {
        static void Main(string[] args)
        {
            
            /* Arrays 
            -- Collection of multiple values under one variable.
            -- Number of elements CANNOT change. 
            -- Conents of elements CAN change. 
            -- Element position in the array is called the INDEX. 
            -- Array indexes start at 0. 
            */ 
                    
            /* Declaring Arrays 
            Method 1 -- Creating Array with Values
            Other methods exist but only this method will be used in class. 
            */             

            // Declare and Define Three Arrays -- string, integer, and float or double v0.1a
            string[] breakfastFoods = {"Bacon", "Waffles", "Pancakes", "Cereal", "Parfait"};
            int[] testScores = {95, 100, 25, 15, 27, 35};
            float[] GPA = {3.14f, 2.25f, 1.74f, 1.99f, 0.99f, 4.25f};

            // Print Array Contents -- All Elements on Single Line v0.1b 
            Console.WriteLine("The contents for each array are:\n");
            Console.WriteLine("breakfastFoods: \n" + String.Join(", ", breakfastFoods));
            Console.WriteLine();
            Console.WriteLine("testScores: \n" + String.Join(", ", testScores));
            Console.WriteLine();
            Console.WriteLine("GPA: \n" + String.Join(", ", GPA));
            Console.WriteLine();

            // Print Array Contents -- One Elements Per Line v0.1c
            Console.WriteLine("The contents for each array are:\n");
            Console.WriteLine("breakfastFoods: \n" + String.Join("\n", breakfastFoods));
            Console.WriteLine();
            Console.WriteLine("testScores: \n" + String.Join("\n", testScores));
            Console.WriteLine();
            Console.WriteLine("GPA: \n" + String.Join("\n", GPA));
            Console.WriteLine();
            
            // Determine Array Length v0.1d
            Console.WriteLine("The length of each array is:");
            Console.WriteLine("breakFastFoods: " + breakfastFoods.Length);
            Console.WriteLine("testScores: " + testScores.Length);
            Console.WriteLine("GPA: " + GPA.Length);
            
            // Access First Element v0.2a
            Console.WriteLine("The first element in each array is:\n");
            Console.WriteLine(breakfastFoods[0]);
            Console.WriteLine(testScores[0]);
            Console.WriteLine(GPA[0]);

            // Access Last Element v0.2b
            Console.WriteLine("The last element in each array is: \n");
            Console.WriteLine(breakfastFoods[breakfastFoods.Length - 1]);
            Console.WriteLine(testScores[testScores.Length -1]);
            Console.WriteLine(GPA[GPA.Length -1]);

            // Access 3rd Element v0.2c -- PWYOC
            Console.WriteLine("The third element in each array is:\n");
            Console.WriteLine(breakfastFoods[2]);
            Console.WriteLine(testScores[2]);
            Console.WriteLine(GPA[2]);

            // Change Elements in Array v0.3a 
            breakfastFoods[0] = "Fried Squid";
            testScores[0] = 59; 
            GPA[0] = 1.34f; 
            Console.WriteLine("The contents for each array are:\n");
            Console.WriteLine("breakfastFoods: \n" + String.Join(", ", breakfastFoods));
            Console.WriteLine();
            Console.WriteLine("testScores: \n" + String.Join(", ", testScores));
            Console.WriteLine();
            Console.WriteLine("GPA: \n" + String.Join(", ", GPA));
            Console.WriteLine();

            // Change Elements in Array 0.3b -- PWYOC
            breakfastFoods[4] = "Greasy Grimy Gopher Guts";
            testScores[4] = 1; 
            GPA[4] = 0.02f; 
            Console.WriteLine("The contents for each array are:\n");
            Console.WriteLine("breakfastFoods: \n" + String.Join(", ", breakfastFoods));
            Console.WriteLine();
            Console.WriteLine("testScores: \n" + String.Join(", ", testScores));
            Console.WriteLine();
            Console.WriteLine("GPA: \n" + String.Join(", ", GPA));
            Console.WriteLine();            

            // Common Array Bugs -- 0.4a 
            // Index Out of Bounds -- Accessing an element that does not exist. 
            // Console.WriteLine(breakFastFoods[5]); 

            // Incorrect Data Types 
            // testScores[0] = "Billy";



            
        }
    }
}
