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

        // CPU Pick Random Choice 
        static int CPUChoice()
        {
            Random r = new Random(); 
            int randChoice = r.Next(0, 3);    
            return randChoice;      
        }
        
        static string PlayerRPS()
        {
            Console.WriteLine("Please type Rock, Paper, or Scissors and press ENTER.\n");
            string choice; 
            choice = Console.ReadLine(); 
            choice = choice[0].ToString();
            choice = choice.ToLower(); 
            if (choice == "r") {
                choice = "rock";
            } else if (choice == "p") {
                choice = "paper";
            } else if (choice == "s") {
                choice = "scissors"; 
            } else {
                Console.WriteLine("Error: Warning Terminal File");
            }
            Console.WriteLine(choice);
            return choice; 
        }
        
        static string DetermineRoundWinner(playerPick, cpuPick)
        {
            Console.WriteLine("You have chosen " + playerPick);
            Console.WriteLine("The CPU has chosen " + cpuPick);
            if (playerPick == "rock" && cpuPick == "rock") {
                Console.WriteLine("That is a draw.\n");
                return "draw"; 
            }
            if (playerPick == "rock" && cpuPick == "scissors") {
                Console.WriteLine("You win.\n");
                return "player"; 
            }
            if (playerPick == "rock" && cpuPick == "paper") {
                Console.WriteLine("You lose.\n");
                return "cpu"; 
            }
        }
        
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
            PlayerRPS(); 
            // int loop = 0; 
            // while (loop < 100) {
            //     Console.WriteLine(choices[CPUChoice()]);
            //     loop++; 
            // }
        }
    }
}
