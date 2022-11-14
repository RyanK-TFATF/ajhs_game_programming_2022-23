// Calculating Hit Boxes, Ryan Kelley, 11/04/22, 1:53PM, v0.2
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

            // Hit Box Area Calculations 
            // Box A 
            int boxA2DArea = boxALength * boxAWidth; 
            int boxA3DArea = boxALength * boxAWidth * boxAHeight; 

            // Box B
            int boxB2DArea = boxBLength * boxBWidth; 
            int boxB3DArea = boxBLength * boxBWidth * boxBHeight;                 

            // Verify Measurements
            Console.WriteLine(String.Format("Box A -- Length: {0} Width: {1} Height: {2}", boxALength, boxAWidth, boxAHeight));
            Console.WriteLine(String.Format("Box B -- Length: {0} Width: {1} Height: {2}", boxBLength, boxBWidth, boxBHeight));

            // Print Area Calculations 
            if (hitBoxType == 1) {
                Console.WriteLine(String.Format("The Box A 2D area is {0} and the Box B 2D area is {1}.", boxA2DArea, boxB2DArea));
            } else if (hitBoxType == 2) {
                Console.WriteLine(String.Format("The Box A 3D area is {0} and the Box B 3D area is {1}.", boxA3DArea, boxB3DArea));
            } else {
                Console.WriteLine("You still did not select the correct hit box type.\n");
                Console.WriteLine("Everyone in this room is now dumber for having seen this.  I award you no points.\n");
                Console.WriteLine("May God have mercy upon your soul.\n");
            }
            
            // Calculate % Difference and Print to Screen 





        }
    }
}
