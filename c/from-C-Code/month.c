
// Function to return the number of days
// in a month
int numberOfDays(int monthNumber, int year)
{
    // January
    if (monthNumber == 0)
        return (31);
  
    // February
    if (monthNumber == 1) {
        // If the year is leap then Feb
        // has 29 days
        if (year % 400 == 0
            || (year % 4 == 0
                && year % 100 != 0))
            return (29);
        else
            return (28);
    }
  
    // March
    if (monthNumber == 2)
        return (31);
  
    // April
    if (monthNumber == 3)
        return (30);
  
    // May
    if (monthNumber == 4)
        return (31);
  
    // June
    if (monthNumber == 5)
        return (30);
  
    // July
    if (monthNumber == 6)
        return (31);
  
    // August
    if (monthNumber == 7)
        return (31);
  
    // September
    if (monthNumber == 8)
        return (30);
  
    // October
    if (monthNumber == 9)
        return (31);
  
    // November
    if (monthNumber == 10)
        return (30);
  
    // December
    if (monthNumber == 11)
        return (31);
}