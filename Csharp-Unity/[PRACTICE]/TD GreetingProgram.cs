using System;

namespace GreetingProgram
{
    class Program
    {
        static DateTime dateCourante = DateTime.Now;
        //Cette variable ne peut que être déclarée dans Program pour qu'elle puisse être accessible ailleurs
        //Les objets statiques ne peuvent que manipuler du statique

        static void Main(string[] args)
        {

            Console.WriteLine(dateCourante);
            Greeting("Henri");
            //une méthode statique ne peut que appeller des méthodes statiques
        }

        static void Greeting(string username)
        {
            if (dateCourante.Hour >= 9 && dateCourante.Hour <= 18)
            {
                switch (dateCourante.DayOfWeek)
                {
                    case DayOfWeek.Monday:
                    case DayOfWeek.Tuesday:
                    case DayOfWeek.Wednesday:
                    case DayOfWeek.Thursday:
                    case DayOfWeek.Friday:
                        Bonjour(username);
                        break;

                    case DayOfWeek.Saturday:
                    case DayOfWeek.Sunday:
                        Bonwe(username);
                        break;
                }
            }
            else if (dateCourante.Hour < 9)
            {
                switch (dateCourante.DayOfWeek)
                {
                    case DayOfWeek.Monday:
                    case DayOfWeek.Saturday:
                    case DayOfWeek.Sunday:
                        Bonwe(username);
                        break;

                    case DayOfWeek.Tuesday:
                    case DayOfWeek.Wednesday:
                    case DayOfWeek.Thursday:
                    case DayOfWeek.Friday:
                        Bonsoir(username);
                        break;
                }
            }

            else
            {
                switch (dateCourante.DayOfWeek)
                {
                    case DayOfWeek.Monday:
                    case DayOfWeek.Tuesday:
                    case DayOfWeek.Wednesday:
                    case DayOfWeek.Thursday:
                        Bonsoir(username);
                        break;

                    case DayOfWeek.Friday:
                    case DayOfWeek.Saturday:
                    case DayOfWeek.Sunday:
                        Bonwe(username);
                        break;

                    default:
                        Console.WriteLine("Error");
                        break;
                }

            }
        }

        static void Bonjour(string userbonjour)
        {

            Console.WriteLine("Bonjour " + userbonjour); //Enrivonment.UserName

        }

        static void Bonsoir(string userbonsoir)
        {

            Console.WriteLine("Bonsoir " + userbonsoir); //Enrivonment.UserName

        }

        static void Bonwe(string userbonwe)
        {

            Console.WriteLine("Bon week-end " + userbonwe); //Enrivonment.UserName

        }

    }
}
