#*-* coding: utf-8 -*-
"""
@file
@brief Uses `pythonnet <https://github.com/sdpython/pythonnet>`_.
"""

import sys, platform, os

if sys.platform.startswith("win") :
    ver = sys.version_info
    arch = platform.architecture()[0]
    if ver[:2] == (3,3) :
        if "64" in arch :
            from .py33x64 import clr
        elif arch == "32bit" :
            from .py33 import clr
        else :
            raise ImportError("unable to import pythonnet for this architecture " + str(arch))
    elif ver[:2] == (3,4) :
        if "64" in arch :
            from .py34x64 import clr
        elif arch == "32bit" :
            from .py34 import clr
        else :
            raise ImportError("unable to import pythonnet for this architecture " + str(arch))
    else :
        raise ImportError("unable to import pythonnet for this version of python " + str(ver))

def vocal_synthesis(text, lang = "fr-FR", voice = "", filename = ""):
    """
    Utilise la synthèse vocale de Windows

    @param      text        text à lire
    @param      lang        langue
    @param      voice       nom de la voix (vide si voix par défaut)
    @param      filename    nom de fichier pour sauver le résultat au format wav (vide sinon)

    @example(techniques___Utiliser une DLL implémentée en C#)
    
    .. index:: C#,DLL
    
    Le code de la DLL est le suivant. Il a été compilé sous forme de DLL.
    @code
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
    @endcode

    Pour l'utiliser, il faut utiliser l'instruction :

    @code
    from ensae_teaching_cs.pythonnet import clr
    from clr import AddReference
    AddReference("ENSAE.Voice")
    @endcode

    Si le programme répond qu'il ne trouve pas le fichier, il suffit
    d'inclure de la répertoire où se trouve la DLL dans la liste ``sys.path``.
    Ensuite on écrit simplement :

    @code
    from ENSAE.Voice import Speech
    Speech.VocalSynthesis(text, lang, voice, filename)
    @endcode
    
    Il faut voir le notebook :ref:`pythoncsharprst`.

    @endexample
    """
    if "ENSAE.Voice" not in sys.modules:
        if not sys.platform.startswith("win") :
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path,"csdll")

        from clr import AddReference

        try:
            AddReference("ENSAE.Voice")
        except Exception as e :
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path,"csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("ENSAE.Voice")

    from ENSAE.Voice import Speech
    Speech.VocalSynthesis(text, lang, voice, filename)

def import_magic_cs():
    """
    import the C# DLL which helps doing C# in a notebooks

    @return     pointer on C# static class
    """
    if "MagicIPython" not in sys.modules:
        if not sys.platform.startswith("win") :
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path,"csdll")

        from clr import AddReference

        try:
            AddReference("MagicIPython")
        except Exception as e :
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path,"csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("MagicIPython")

    from MagicIPython import MagicCS
    return MagicCS