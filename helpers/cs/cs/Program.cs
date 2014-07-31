using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ENSAE.Voice;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
            Speech.VocalSynthesis("test unitaire", "fr-FR", null, null);
            Console.WriteLine();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();

        }
    }
}
