// Calc. Hit Boxes, Ryan Kelley, 11/07/22, v0.2 
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

            // Input Measurements Box A
            Console.WriteLine("Please enter the LENGTH for HIT BOX A. ");
            hitBoxALength = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Please enter the WIDTH for HIT BOX A. ");
            hitBoxAWidth = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Please enter the HEIGHT for HIT BOX A. ");
            hitBoxAHeight = Convert.ToInt32(Console.ReadLine()); 

            // Input Measurements Box B
            Console.WriteLine("Please enter the LENGTH for HIT BOX B. ");
            hitBoxBLength = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Please enter the WIDTH for HIT BOX B. ");
            hitBoxBWidth = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Please enter the HEIGHT for HIT BOX B. ");
            hitBoxBHeight = Convert.ToInt32(Console.ReadLine()); 


            // 2D Hit Box Calculations 
            int hitBoxA2Darea = hitBoxALength * hitBoxAWidth; 
            int hitBoxB2Darea = hitBoxBLength * hitBoxBWidth; 

            // 3D Hit Box Calculations 
            int hitBoxAVolume = hitBoxALength * hitBoxAWidth * hitBoxAHeight; 
            int hitBoxBVolume = hitBoxBLength * hitBoxBWidth * hitBoxBHeight; 

            // Verify Measurements 
            Console.WriteLine(String.Format("Box A Measurements -- Length: {0} Width: {1} Height: {2}.", hitBoxALength,hitBoxAWidth,hitBoxAHeight));
            Console.WriteLine(String.Format("Box B Measurements -- Length: {0} Width: {1} Height: {2}.", hitBoxBLength,hitBoxBWidth,hitBoxBHeight));
            
            // Print Calculations to Screen 
            if (hitBoxType == 1) {
                Console.WriteLine("Box A Area is {0}.", hitBoxA2Darea);
                Console.WriteLine("Box B Area is {0}.", hitBoxB2Darea);
            } else if (hitBoxType == 2) {
                Console.WriteLine("Box A Volume is {0}.", hitBoxAVolume);
                Console.WriteLine("Box B Volume is {0}.", hitBoxBVolume);
            } else {
                Console.WriteLine("Invalid Hit Box Type Selected.  Please restart.");
            }

            // Calculate % Difference 
            // Declare New Variables 
            int diff = 0; // Difference between the two calculations. 
            float avg = 0; // Average of the two calculations.  
            float diffDivAvg = 0; // Difference divided by average. 
            float percentDiff = 0; // Calculate % Difference 

            if (hitBoxType == 1 && hitBoxA2Darea > hitBoxB2Darea) {
                Console.WriteLine("Box A is larger than Box B.");
                diff = hitBoxA2Darea - hitBoxB2Darea;
                avg = (hitBoxA2Darea + hitBoxB2Darea) / 2; 
                diffDivAvg = diff / avg;
                percentDiff = diffDivAvg * 100; 
                Console.WriteLine(String.Format("Box A is {0}% larger than Box B.", percentDiff));
            } else if (hitBoxType == 1 && hitBoxB2Darea > hitBoxA2Darea) {
                Console.WriteLine("Box B is larger than Box A.");
                 diff = hitBoxA2Darea - hitBoxB2Darea;
                avg = (hitBoxA2Darea + hitBoxB2Darea) / 2; 
                diffDivAvg = diff / avg;
                percentDiff = diffDivAvg * 100; 
                Console.WriteLine(String.Format("Box A is {0}% larger than Box B.", percentDiff));
            } else if (hitBoxType == 1 && hitBoxB2Darea == hitBoxA2Darea) { 
                Console.WriteLine("Box B is equal to Box A.");
            } else if (hitBoxType == 2 && hitBoxAVolume > hitBoxBVolume) {
                Console.WriteLine("Box A is larger than Box B.");
            } else if (hitBoxType == 2 && hitBoxBVolume > hitBoxAVolume) {
                Console.WriteLine("Box B is larger than Box A.");
            } else if (hitBoxType == 2 && hitBoxAVolume == hitBoxBVolume) {
                Console.WriteLine("Box B is equal to Box A.");
            } else {
                Console.WriteLine("CRITICAL ERROR. UNABLE TO COMPUTE. PLEASE RESTART.");
            }


        }
    }
}
