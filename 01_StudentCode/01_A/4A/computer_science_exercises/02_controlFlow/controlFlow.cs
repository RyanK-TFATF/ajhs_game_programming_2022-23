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

        }
    }
}
