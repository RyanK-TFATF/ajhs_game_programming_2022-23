// Calc. Hit Boxes, Ryan KElley, 11/07/22, v0.2 
using System;

namespace _01_CalculatingHitBoxes
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaring Variables 
            // 2D or 3D Hit Box? 
            int hitBoxType = 0; // 1 = 2D hit box, 2 = 3D hit box 
            Console.WriteLine("Please select a hit box type: Enter 1 for 2D, 2 for 3D.");
            hitBoxType = Convert.ToInt32(Console.ReadLine()); 
            if (hitBoxType == 1) {
                Console.WriteLine("You have chosen a 2D hit box model.");
            } else if (hitBoxType == 2) {
                Console.WriteLine("You have chosen a 3D hit box model.");
            } else {
                Console.WriteLine("ERROR: Incorrect model selected, please try again.");
                Console.WriteLine("Please select a hit box type: Enter 1 for 2D, 2 for 3D.");
                hitBoxType = Convert.ToInt32(Console.ReadLine()); 
            }

            // Hit Box A Measurements 
            int hitBoxALength = 0; 
            int hitBoxAWidth = 0; 
            int hitBoxAHeight = 0; 

            // Hit Box B Measurements 
            int hitBoxBLength = 0; 
            int hitBoxBWidth = 0; 
            int hitBoxBHeight = 0;

            // Input Measurements 
            Console.WriteLine("Please enter the LENGTH for HIT BOX A. ");
            hitBoxALength = Convert.ToInt32(Console.ReadLine()); 

            // 2D Hit Box Calculations 
            int hitBoxA2Darea = hitBoxALength * hitBoxAWidth; 
            int hitBoxB2Darea = hitBoxBLength * hitBoxBWidth; 

            // 3D Hit Box Calculations 
            int hitBoxA3Darea = hitBoxALength * hitBoxAWidth * hitBoxAHeight; 
            int hitBoxB3Darea = hitBoxBLength * hitBoxBWidth * hitBoxBHeight; 

            // Print Area 
            Console.WriteLine(hitBoxA2Darea); 
            // Box B 2D Area
            // Box A 3D Area
            // Box B 3D Area 

        }
    }
}
