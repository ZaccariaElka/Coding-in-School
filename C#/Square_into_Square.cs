using System;
using System.Collections.Concurrent;

namespace HelloWorld
{
class Program
{
    static void Main(string[] args)
    {
        string s = "[]";                        // symbol
        string space = "__";                    // "space" symbol
        int l = 11;                             // length

        for (int j = 0; j < l; j++) {           // outer loop

            for (int i = 0; i < l; i++)         // inner loop

            {

                if (i == 0 ||                   // check first row
                        j == 0 ||                   // check first column

                        i == l - 1 ||               // check last row
                        j == l - 1 ||               // check last column

                        i == j ||                   // diagonal left
                        i == (l - 1) - j ||         // diagonal right

                        j == l / 2 ||               // axis x
                        i == l / 2 ||               // axis y

                        i == l / 2 - j ||           // diagonal up left
                        j == l / 2 + i ||           // diagonal down left

                        i - j == (l / 2) ||         // diagonal up right
                        i + j == (l / 2 - 1) + l    // diagonal down left

                   )

                {

                    Console.Write(s);           // prints "s" if true
                } else {
                    Console.Write(space);       // prints spaces if false
                }


            }
            Console.WriteLine();                // goes ahead

        }





    }
}
}