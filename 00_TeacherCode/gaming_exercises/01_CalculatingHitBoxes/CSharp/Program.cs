// Calculating Hit Boxes, Ryan Kelley, 11/04/22, 12:26PM, v0.2a

using System;

namespace _01_CalculatingHitBoxes
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variable Declarataions       
            // int hitBoxType = 0; // 1 = 2D hit box, 2 = 3D hit box

            // Hit Box A Measurements 
            int hitBoxALength = 0; 
            int hitBoxAWidth = 0; 
            int hitBoxAHeight = 0; 
            
            
            // Hit Box B Measurements 
            int hitBoxBLength = 0; 
            int hitBoxBWidth = 0; 
            int hitBoxBHeight = 0; 

            // 2D Hit Box Calculations
            int area2DHitBoxA = hitBoxALength * hitBoxAWidth;
            int area2DHitBoxB = hitBoxBLength * hitBoxBWidth;
                    
            // 3D Hit Box Calculations
            int area3DHitBoxA = hitBoxALength * hitBoxAWidth * hitBoxAHeight;
            int area3DHitBoxB = hitBoxBLength * hitBoxBWidth * hitBoxBHeight;


        }
    }
}
