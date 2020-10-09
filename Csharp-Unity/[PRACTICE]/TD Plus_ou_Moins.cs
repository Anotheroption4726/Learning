using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TD_Plus_ou_Moins
{
    class Program
    {
        static Random rnd = new Random();
        static int valeurATrouver;
        static int compteur = 1;

        static void Main(string[] args)
        {
            valeurATrouver = new Random().Next(0, 100);
            Jeu();
        }

        static void Jeu()
        {
            int nombreChoisi;
            bool finDuJeu = false;


            while (finDuJeu == false)
            {
                Console.WriteLine("Veuillez saisir un nombre entre 0 et 99 et valider avec la touche \"Entrée\"");
                string saisie = Console.ReadLine();

                if (int.TryParse(saisie, out nombreChoisi) && nombreChoisi >= 0 && nombreChoisi < 100)
                {
                    Console.WriteLine("Vous avez saisi : " + nombreChoisi);
                    
                    if (nombreChoisi < valeurATrouver)
                    {
                        Console.WriteLine("Le nombre est trop petit");
                        compteur++;
                    }
                    else if (nombreChoisi > valeurATrouver)
                    {
                        Console.WriteLine("Le nombre est trop grand");
                        compteur++;
                    }
                    else
                    {
                        Console.WriteLine("Bravo vous avez trouvé après " + compteur + " essais!");
                        finDuJeu = true;
                    }
                }
                else
                {
                    Console.WriteLine("Erreur. Veuillez choisir un nombre entre 0 et 99.");
                }

            }


        }

    }
}
