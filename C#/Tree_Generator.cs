
using System.Transactions;
using System.Threading;

class Program
{
    static void Main(string[] args)
    {

        static void tree()
        {
            string symbol = "  "; // what we are going to use to draw the tree
            string space = "  "; // "spaces" to fill empty places

            Console.WriteLine("Inset one of these number: 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47");
            string number = Console.ReadLine(); // size of the trees
            int size = Convert.ToInt32(number); // converts "number" to int 

            if (size == 5 || size == 7 || size == 11 || size == 13 || size == 17 || size == 19 || size == 23 || size == 29 || size == 31 || size == 37 || size == 41 || size == 43 || size == 47)
            { //check if the number is a prime number

                for (int y = 0; y < size; y++) // loop y
                {
                    for (int x = 0; x < size; x++) // loop x
                    {

                        int primenumber = (y * 2) + 1; // find the prime number for the triangle
                        int halftriangle = size / 2; // find the half of the triangle's size
                        int loopsize = size - 1; // the loop starts from 0 so we remove a value from the size


                        if (
                            x == halftriangle || // axis x
                            y == halftriangle || // axis y
                            x > (loopsize - primenumber) / 2 && x < halftriangle && y < halftriangle || // half triangle left
                            x <= ((loopsize) / 2 + primenumber / 2) && y < halftriangle && x >= halftriangle // half triangle right
                            )
                        {

                            if ( y <= halftriangle ) // check if y is over the half
                            {
                                Console.BackgroundColor = ConsoleColor.Green; // change the color of the console
                                Console.Write(symbol); // if the statements are true it's gonna print the symbol
                                Console.ResetColor(); // reset console color
                            } else
                            {
                                Console.BackgroundColor = ConsoleColor.DarkRed ^ ConsoleColor.Black; // change the color of the console
                                Console.Write(symbol); // if the statements are true it's gonna print the symbol
                                Console.ResetColor(); // reset console color
                            }
                        }
                        else
                        {
                            Console.Write(space); // prints a space into the console
                        }

                    } // end loop x
                    Console.WriteLine(); // go ahead every time the loop y is fully completed
                } // end loop y

            } // end of prime check
            else
            {
                Console.WriteLine("invalid number."); // prints message if the number is not valid
                Thread.Sleep(2000); // waits 2 seconds
                Console.Clear();
                tree();
            }
        }

        tree(); // i used a function to make the whole code repeat if the user interts an invalid number. I could have used other ways but i wanted to try this one
        
    }
}
  