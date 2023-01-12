// 03_Inventory, Ryan Kelley, v0.0 
using System;
using System.Collections; 

namespace _03_Inventory
{
    class Program
    {
        // Method Declarations 
        // Method Signature defines the return types, parameters, and name.
        static void DisplayInventory(ArrayList inventory) 
        {
            Console.WriteLine("You peek into your backpack and find:");
            foreach (string item in inventory)   {
                Console.WriteLine(item);
            }
        }

        static void DisplayWeapons(List<bool[]> weapons)
        {
            int weaponCounter = 0; 
            while (weaponCounter < weapons.Length)
            {
                if (weaponCounter == 0 && weapons[weaponCounter] == true) {
                    Console.WriteLine("You are equipped with the chainsaw.");
                }
                weaponCounter++; 
            }
        }
        static void Main(string[] args)
        {
            var playerInventory = new ArrayList()
            {
                "blue health potion",
                "green mana potion",
                "bronze sword",
                "bronze shield",
                "steel helmet",
                "steel armor",
                "torch",
                "turkey leg",
                "beef jerky", 
                "lantern"
            }; 
            // Call Method 
            //DisplayInventory(playerInventory); 

           

        }
    }
}
