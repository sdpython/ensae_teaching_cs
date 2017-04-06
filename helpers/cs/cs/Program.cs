using System;
using System.IO;
using ENSAE.Voice;
using System.Speech.Recognition;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
            var voices = Speech.GetVoiceForVocalSynthesis();
            string filename = @"C:\xadupre\__home_\GitHub\jupytalk\_unittests\ut_mokadi\data\output.wav";
            Console.WriteLine("reco file");
            var resR = SpeechRecoSystem.Recognize(filename);
            Console.WriteLine("{0}", resR);
            Console.WriteLine("reco wav");
            resR = SpeechRecoSystem.Recognize(File.ReadAllBytes(filename));
            Console.WriteLine("{0}", resR);
            foreach(var item in SpeechRecoSystem.EnumerateRecognize())
                Console.WriteLine("{0} - {1}", item.Item1, item.Item2);

            string subkey = null;
            if (!string.IsNullOrEmpty(subkey))
            {
                var res = SpeechReco.RunReco(subkey, @"C:\temp\output.wav");
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
