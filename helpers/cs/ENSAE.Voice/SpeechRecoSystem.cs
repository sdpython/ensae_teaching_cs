using System;
using System.Collections.Generic;
using System.Speech.Recognition;
using System.IO;

namespace ENSAE.Voice
{
    public class SpeechRecoSystem : IDisposable
    {
        public static Tuple<float, string>[] Recognize(byte[] wav, string culture = "fr-FR")
        {
            using (var engine = new SpeechRecoSystem())
            {
                var results = new List<Tuple<float, string>>();
                engine.Feed(wav);
                var res = engine.WaitForText(1);
                int loop = 2;
                while (res == null && loop > 0)
                {
                    --loop;
                    res = engine.WaitForText(1);
                }
                results.Add(new Tuple<float, string>(res.Confidence, res.Text));
                return results.ToArray();
            }
        }

        public static Tuple<float, string>[] Recognize(string wav, string culture = "fr-FR")
        {
            using (var engine = new SpeechRecoSystem())
            {
                var results = new List<Tuple<float, string>>();
                var res = engine.Feed(wav);
                results.Add(new Tuple<float, string>(res.Confidence, res.Text));
                return results.ToArray();
            }
        }

        Queue<RecognitionResult> queue;
        SpeechRecognitionEngine _recognizer;

        public SpeechRecoSystem(string culture = "fr-FR")
        {
            queue = new Queue<RecognitionResult>();

            _recognizer = new SpeechRecognitionEngine(new System.Globalization.CultureInfo("fr-FR"));
            _recognizer.LoadGrammar(new DictationGrammar());
            _recognizer.SpeechRecognized +=
              new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);
        }

        void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            queue.Enqueue(e.Result);
        }

        public RecognitionResult Feed(string wav)
        {
            _recognizer.SetInputToWaveFile(wav);
            return _recognizer.Recognize();
        }

        public RecognitionResult Feed(byte[] wav)
        {
            using (var fs = new MemoryStream(wav, false))
                _recognizer.SetInputToWaveStream(fs);
            return _recognizer.Recognize();
        }

        public void Feed()
        {
            _recognizer.SetInputToDefaultAudioDevice();
            _recognizer.RecognizeAsync(RecognizeMode.Multiple);
        }

        public void Dispose()
        {
            _recognizer.Dispose();
        }

        public RecognitionResult WaitForText(int maxloop = 5, int delay=1000)
        {
            while (queue.Count == 0 && maxloop > 0)
            {
                System.Threading.Thread.Sleep(delay);
                --maxloop;
            }
            return queue.Count == 0 ? null : queue.Dequeue();
        }
    }
}
