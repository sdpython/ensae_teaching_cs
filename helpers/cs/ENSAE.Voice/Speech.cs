﻿using System.Speech.Synthesis;
using System.Globalization;

namespace ENSAE.Voice
{
    public static class Speech
    {
        public static void VocalSynthesis(string text, string culture, string filename, string voice)
        {
            SpeechSynthesizer synth = new SpeechSynthesizer();

            synth.SelectVoiceByHints(VoiceGender.Neutral, VoiceAge.NotSet, 1, new CultureInfo(culture));

            if (!string.IsNullOrEmpty(filename))
                synth.SetOutputToWaveFile(filename);
            if (!string.IsNullOrEmpty(voice))
                synth.SelectVoice(voice);

            synth.Speak(text);
        }
    }
}
