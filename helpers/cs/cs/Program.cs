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
            string filename = @"jupytalk\_unittests\ut_mokadi\data\output.wav";
            var resR = SpeechRecoSystem.Recognize(File.ReadAllBytes(filename));
            for(int i = 0; i < resR.Length;++i)
                Console.WriteLine("{0} - {1}", resR[i].Item1, resR[i].Item2);

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
