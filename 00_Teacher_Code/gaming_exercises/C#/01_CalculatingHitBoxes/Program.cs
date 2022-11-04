// Calculating Hit Boxes, Ryan Kelley, 11/04/22, 12:26PM, v0.2

using System;

namespace _01_CalculatingHitBoxes
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variable Declarataions       
            int hitBoxType = 0; // 1 = 2D hit box, 2 = 3D hit box

            // 2D Hit Box Measurements 
            int hitBox2DLengthA = 0; 
            int hitBox2DWidthA = 0; 
            int hitBox2DLengthB = 0; 
            int hitBox2DWidthB = 0; 

            // 2D Hit Box Calculations
            int area2DHitBoxA = hitBox2DLengthA * hitBox2DWidthA;
            int area2DHitBoxB = hitBox2DLengthB * hitBox2DWidthB;

            // 3D Hit Box Measurements 
            int hitBox3DLengthA = 0; 
            int hitBox3DWidthA = 0; 
            int hitBox3DHeightA = 0; 
            int hitBox3DLengthB = 0; 
            int hitBox3DWidthB = 0; 
            int hitBox3DHeightB = 0; 
            
            // 2D Hit Box Calculations
            int area3DHitBoxA = hitBox3DLengthA * hitBox3DWidthA * hitBox3DHeightA;
            int area3DHitBoxB = hitBox3DLengthB * hitBox3DWidthB * hitBox3DHeightB;

        }
    }
}
