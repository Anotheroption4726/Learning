using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculs
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine(CalculSommeEntiers(1, 10));
            Console.WriteLine(CalculSommeEntiers(1, 100));

            List<double> listeMoyenne = new List<double> { 1.0, 5.5, 9.9, 2.8, 9.6 };
            Console.WriteLine(CalculMoyenne(listeMoyenne));

            Console.WriteLine(TroisiemeMethode());
            Console.WriteLine(CalculSommeIntersection());

        }

        static int CalculSommeEntiers (int x, int y)
        {

            int total = 0;

            while (x <= y)
            {
                total += x;
                x++;
            }

            return total;

        }


        static double CalculMoyenne(List<double> listeDoubles)
        {

            double total = 0;

            foreach (double nombre in listeDoubles)
            {
                total += nombre;
            }

            return total/listeDoubles.Count;

        }

        static int TroisiemeMethode()
        {

            int total = 0;
            List<int> listeTrois = new List<int> {};
            List<int> listeCinq = new List<int>();

            for (int multipleTrois = 3; multipleTrois < 100; multipleTrois += 3)
            {
                listeTrois.Add(multipleTrois);
                //Console.WriteLine(multipleTrois);
            }

            for (int multipleCinq = 5; multipleCinq < 100; multipleCinq += 5)
            {

                listeCinq.Add(multipleCinq);
                //Console.WriteLine(multipleCinq);

                foreach (int nombre in listeTrois)
                {
                    if (nombre == multipleCinq)
                    {
                        total += nombre;
                        //Console.WriteLine(nombre);
                    }
                }

            }

            return total;

        }


        static int CalculSommeIntersection()
        {
            List<int> multiplesDe3 = new List<int>();
            List<int> multiplesDe5 = new List<int>();

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0)
                    multiplesDe3.Add(i);
                if (i % 5 == 0)
                    multiplesDe5.Add(i);
            }

            int somme = 0;
            foreach (int m3 in multiplesDe3)
            {
                foreach (int m5 in multiplesDe5)
                {
                    if (m3 == m5)
                        somme += m3;
                }
            }
            return somme;
        }


    }
}
