// Rock Paper Scissors, ryan kelley, v0.0
using System;

namespace _04_RockPaperScissors
{

    
    class Program
    {
        static void DisplayMenu()
        {
            Console.WriteLine("+*************************************+");
            Console.WriteLine("+           Welcome to                +");
            Console.WriteLine("+ Ryan's Rock-Paper-Scissors Robot!   +");
            Console.WriteLine("+                                     +");
            Console.WriteLine("+ You will choose Rock, Paper, or     +");
            Console.WriteLine("+ Scissors.                           +");
            Console.WriteLine("+                                     +");
            Console.WriteLine("+ The CPU will do the same.           +");
            Console.WriteLine("+ A winner is chosen based on this:   +");
            Console.WriteLine("+ Rock Beats Scissors                 +");
            Console.WriteLine("+ Paper Beats Rock                    +");
            Console.WriteLine("+ Scissors Beats Paper                +");
            Console.WriteLine("+                                     +");
            Console.WriteLine("+ The winner of each round will earn  +");
            Console.WriteLine("+ one point.                          +");
            Console.WriteLine("+                                     +");
            Console.WriteLine("+ First player to earn three points   +");
            Console.WriteLine("+ will win the match.                 +");
            Console.WriteLine("+*************************************+");
        }

        /* static string CPUChoice()
        {
            return 
        }
        */ 
        static void Main(string[] args)
        {
            // DisplayMenu();
            // Declare Important Variables 
            string playerPick = ""; 
            string cpuPick = ""; 

            int playerScore = 0; 
            int cpuScore = 0; 

            string[] choices = {
                "rock",
                "paper",
                "scissors"
            }; 

            

        }
    }
}
