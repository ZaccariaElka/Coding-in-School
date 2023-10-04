using System;

namespace HelloWorld
{
class Program
{
    static void Main(string[] args)
    {

        Console.WriteLine("Write something.");
        string x = Console.ReadLine();



        int countvowel = 0; 
        int countother = 0;


        int acount = 0;
        int ecount = 0;
        int icount = 0;
        int ocount = 0;
        int ucount = 0;


        string y = x.ToLower();

        Console.Clear();

        for (int i = 0; i < x.Length; i++) {
            if (y[i] == 'a') {

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{x[i]}");
                Console.ResetColor();

                countvowel++;
                acount++;
            } else if (y[i] == 'e') {

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{x[i]}");
                Console.ResetColor();

                countvowel++;
                ecount++;
            } else if (y[i] == 'i') {

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{x[i]}");
                Console.ResetColor();

                countvowel++;
                icount++;
            } else if (y[i] == 'o') {

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{x[i]}");
                Console.ResetColor();

                countvowel++;
                ocount++;
            } else if (y[i] == 'u') {

                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write($"{x[i]}");
                Console.ResetColor();

                countvowel++;
                ucount++;
            } else {
                Console.Write($"{x[i]}");

                countother++;

            }

            if (i == x.Length - 1) {
                float sum = countvowel + countother;
                float vowelpercentage = 100 / sum * countvowel;

                Console.WriteLine($"\n\n----Stats----");
                Console.WriteLine($"Vowels: {countvowel}");
                Console.WriteLine($"Vowel Percentage: {Math.Round(vowelpercentage)}%\n");

                Console.WriteLine($"A: {acount} - {Math.Round(100 / sum * acount)}%");
                Console.WriteLine($"E: {ecount} - {Math.Round(100 / sum * ecount)}%");
                Console.WriteLine($"I: {icount} - {Math.Round(100 / sum * icount)}%");
                Console.WriteLine($"O: {ocount} - {Math.Round(100 / sum * ocount)}%");
                Console.WriteLine($"U: {ucount} - {Math.Round(100 / sum * ucount)}%");


            }
        }


    }
}
}