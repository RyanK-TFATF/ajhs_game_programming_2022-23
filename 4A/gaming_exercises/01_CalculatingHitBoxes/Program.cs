﻿// Calculating Hit Boxes, Ryan Kelley, 11/04/22, 1:53PM, v0.2
using System;

namespace _01_CalculatingHitBoxes
{
    class Program
    {
        static void Main(string[] args)
        {
            // Hit Box Type Selection 
            int hitBoxType = 0; // 2D = 1, 3D = 2
            Console.WriteLine("Please select a hit box type: 1 for 2D, 2 for 3D.");
            hitBoxType = Convert.ToInt32(Console.ReadLine());
            if (hitBoxType == 1) {
                Console.WriteLine("You have chosen a 2D hit box model.\n");    
            } else if (hitBoxType == 2) {
                Console.WriteLine("You have chosen a 3D hit box model.\n");    
            } else {
                Console.WriteLine("ERROR: Hit Box Type Not Identified!\n");    
                Console.WriteLine("Please select a hit box type: 1 for 2D, 2 for 3D.");
                hitBoxType = Convert.ToInt32(Console.ReadLine());
            }
            
            // Hit Box A Measurements 
            int boxALength = 0; 
            int boxAWidth = 0; 
            int boxAHeight = 0; 

            // Hit Box B Measurements 
            int boxBLength = 0; 
            int boxBWidth = 0; 
            int boxBHeight = 0; 

            // Hit Box Area Calculations 
            // Box A 
            int boxA2DArea = boxALength * boxAWidth; 
            int boxA3DArea = boxALength * boxAWidth * boxAHeight; 

            // Box B
            int boxB2DArea = boxBLength * boxBWidth; 
            int boxB3DArea = boxBLength * boxBWidth * boxBHeight; 

            // Hit Box A Measurments 
            Console.WriteLine("Please enter the LENGTH of Hit Box A:\n");
            boxALength = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter the WIDTH of Hit Box A:\n");
            boxAWidth = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter the HEIGHT of Hit Box A:\n");
            boxAHeight = Convert.ToInt32(Console.ReadLine());

            // Hit Box B Measurments 
            Console.WriteLine("Please enter the LENGTH of Hit Box B:\n");
            boxBLength = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter the WIDTH of Hit Box B:\n");
            boxBWidth = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Please enter the HEIGHT of Hit Box B:\n");
            boxBHeight = Convert.ToInt32(Console.ReadLine());

            // Verify Measurements
            Console.WriteLine(String.Format("Box A -- Length: {0} Width: {1} Height: {2}", boxALength, boxAWidth, boxAHeight));






        }
    }
}
