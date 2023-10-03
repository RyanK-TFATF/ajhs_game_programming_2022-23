// Ryan Kelley, Program Template, v0.01
using System; 

namespace controlFlow 
{
    class controlFlow 
    {
        static void Main(string[] args)
        {
            // DECLARATIONS 
            string favColor = "Blue"; 
            int luckyNumber = -5; 
            float myGPA = 1.33F;
            int myAge = 43; 
            bool pineappleOnPizza = true; 
            /*
            // if Statements -- Check for a single condition!
            if (favColor == "Green") {
                Console.WriteLine("Green with envy!");
            }

            if (luckyNumber % 2 == 0 ) {
                Console.WriteLine("Your lucky number is even!");
            }

            // if - else Statement -- Checks for a single condition, but has two actions. 
            if (myAge > 15) {
                Console.WriteLine("You are eligible to drive");                
            } else {
                Console.WriteLine("START WALKING SCRUB!");
            }

            // if -- else if -- else -- Checks multiple outcomes. 
            if (myGPA == 4.0F) {
                Console.WriteLine("Congrats on straight A grades!");                
            } else if (myGPA >= 3.0F) {
                Console.WriteLine("Congrats on making honor roll!");                
            } else if (myGPA >= 2.0F) {
                Console.WriteLine("You are graduation ready!");                
            } else {
                Console.WriteLine("You should probably study!");                
            }
            // WHEN CHECKING NUMBER VALUES, START WITH THE HIGHEST VALUE!!!!

            if (myGPA >= 2.0F) {
                Console.WriteLine("You are graduation ready!");                     
            } else if (myGPA >= 3.0F) {
                Console.WriteLine("Congrats on making honor roll!");                
            } else if (myGPA == 4.0F) {
                Console.WriteLine("Congrats on straight A grades!");                           
            } else {
                Console.WriteLine("You should probably study!");                
            }

            // Nested Statements 
            if (pineappleOnPizza == true) {
                Console.WriteLine("Eww, that's gross. You must be a boomer.  How old are you?");
                if (myAge > 60) {
                    Console.WriteLine("Just as I suspected! What was it like having a dinosaur growing up?");
                } else {
                    Console.WriteLine("Ok, so you're not a boomer but still have no taste in food.");
                }
            } else {
                Console.WriteLine("Glad to see you have common sense!"); 
            }
            */ 
            // for Loop -- Best for when you know # of iterations needed.
            /* 
                for (statement1; statement2; statement3) {
                Code to loop.
            }
            statement1 is executed ONCE BEFORE the loop starts. 
            statement2 is a CONDITIONAL that is checked EVERYTIME BEFORE loop starts. 
            statement3 is executed EVERYTIME after the loop executes. 
            */ 
            /*
            for (int i = 0; i < 101; i++) {
                Console.WriteLine("" + i);
            }

            // Create your own loop that counts down from 100 to 0. 
            for (int i = 100; i > -1; i--) {
                Console.WriteLine("" + i);
            }
            
            // Nested loops 
            // Outer Loop
            for (int i = 1; i <= 2; i++) {
                Console.WriteLine("Outer: " + i); 

                for (int j = 1; j <= 3; j++) {
                    Console.WriteLine("Inner: " + j);
                }
            }

            // while loop -- Best used when # of iterations needed is unknown
            int x = 0; 
            while (x < 1000) {
                Console.WriteLine("" + x);
                x++; 
            }
            
            // Special Keywords 
            // break will immediately exit a LOOP or an IF/ELSE IF/ELSE block.
            for (int i = 0; i < 101; i++) {
                Console.WriteLine("" + i);
                if (i == 50) {
                    break;
                }
            }
            */ 
            // continue will SKIP the current iteration and then finish the loop.
            for (int i = 0; i < 101; i++) {
                Console.WriteLine("" + i);
                if (i == 50) {
                    continue;
                }
            }

        }
    }
}
