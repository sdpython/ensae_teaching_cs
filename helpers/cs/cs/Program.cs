using System;
using System.IO;
using ENSAE.Voice;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
            string subkey = null;
            if (!string.IsNullOrEmpty(subkey))
            {
                string res = SpeechReco.RunReco(subkey, @"C:\temp\output.wav");
                Console.WriteLine(res);
                var content = File.ReadAllBytes(@"C:\temp\output.wav");
                res = SpeechReco.RunReco(subkey, content);
                Console.WriteLine(res);
            }

            Speech.VocalSynthesis("test unitaire", "fr-FR", null, null);
            Console.WriteLine();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
