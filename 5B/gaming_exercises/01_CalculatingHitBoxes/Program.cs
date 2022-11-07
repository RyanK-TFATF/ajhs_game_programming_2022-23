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

            // Hit Box A Measurements 
            int hitBoxALength = 0; 
            int hitBoxAWidth = 0; 
            int hitBoxAHeight = 0; 

            // Hit Box B Measurements 
            int hitBoxBLength = 0; 
            int hitBoxBWidth = 0; 
            int hitBoxBHeight = 0;

            // 2D Hit Box Calculations 
            int hitBoxA2Darea = hitBoxALength * hitBoxAWidth; 
            int hitBoxB2Darea = hitBoxBLength * hitBoxBWidth; 

            // 3D Hit Box Calculations 
            int hitBoxA3Darea = hitBoxALength * hitBoxAWidth * hitBoxAHeight; 
            int hitBoxB3Darea = hitBoxBLength * hitBoxBWidth * hitBoxBHeight; 


        }
    }
}
