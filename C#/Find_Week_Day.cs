// (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7

int d = 24;
int m = 10;
int y = 2023;


int yy = y % 100; // last 2 digits of the year

//yc = (yy + (yy div 4)) mod 7
int yc = (yy + yy / 4) % 7; // year code

int mc = 0;

switch (m) // month code
{
    case 1:
        mc = 0;
        break;

    case 2:
        mc = 3;
        break;

    case 3:
        mc = 3;
        break;

    case 4:
        mc = 6;
        break;

    case 5:
        mc = 1;
        break;

    case 6:
        mc = 4;
        break;

    case 7:
        mc = 6;
        break;

    case 8:
        mc = 2;
        break;

    case 9:
        mc = 5;
        break;

    case 10:
        mc = 0;
        break;

    case 11:
        mc = 3;
        break;

    case 12:
        mc = 5;
        break;
}

int cc = 0; // century code

if (y >= 1700 && y <= 1799)
{
    cc = 4;
}
else if (y >= 1800 && y <= 1899)
{
    cc = 2;
}
else if (y >= 1900 && y <= 1999)
{
    cc = 0;
}
else if (y >= 2000 && y <= 2099)
{
    cc = 6;
}
else if (y >= 2100 && y <= 2199)
{
    cc = 4;
}
else if (y >= 2200 && y <= 2299)
{
    cc = 2;
}
else if (y >= 2300 && y <= 2399)
{
    cc = 0;
}

int lp = 0; // leap year

if (DateTime.IsLeapYear(y))
{
    lp = 1;
}
else
{
    lp = 0;
}


int calculate = yc + mc + cc + d - lp;

if (m == 1 || m == 2)
{
    calculate = calculate - 1;
}

int result = calculate % 7;

string weekday = "";

switch (result)
{
    case 0:
        weekday = "Sunday";
        break;

    case 1:
        weekday = "Monday";
        break;

    case 2:
        weekday = "Tuesday";
        break;

    case 3:
        weekday = "Wednesday";
        break;

    case 4:
        weekday = "Thursday";
        break;

    case 5:
        weekday = "Friday";
        break;

    case 6:
        weekday = "Saturday";
        break;

}


Console.WriteLine($"{d} {m}, {y}");
Console.WriteLine("---");
Console.WriteLine($"{yy} (yy)");
Console.WriteLine($"{yc} (year code)");
Console.WriteLine($"{mc} (month code)");
Console.WriteLine($"{cc} (century code)");
Console.WriteLine($"{d} (day code)");
Console.WriteLine($"{lp} (leap year)");
Console.WriteLine("---");
Console.WriteLine($"{result} ({weekday})");

