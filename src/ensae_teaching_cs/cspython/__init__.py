# *-* coding: utf-8 -*-
"""
@file
@brief Uses `pythonnet <https://github.com/sdpython/pythonnet>`_.

.. faqref::
    :tag: windows
    :title: Unhandled Exception: System.IO.FileLoadException when using Python.Runtime.dll with Python 3.5)

    When running for the first time on Python 3.5, the following error came up::

        Unhandled Exception: System.IO.FileLoadException: Could not load file or assembly
            'file:///<apath>\\Python.Runtime.dll' or one of its dependencies.
        Operation is not supported. (Exception from HRESULT: 0x80131515) --->
            System.NotSupportedException: An attempt was made to load an assembly
        from a network location which would have caused the assembly to be sandboxed in previous versions of the .NET Framework.
        This release of the .NET Framework does not enable CAS policy by default, so this load may be dangerous.
        If this load is not intended to sandbox the assembly,
        please enable the loadFromRemoteSources switch.
        See http://go.microsoft.com/fwlink/?LinkId=155569 for more information.
        --- End of inner exception stack trace ---
        at System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity,
            RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound,
            Boolean forIntrospection, Boolean suppressSecurityChecks)
        at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef,
            Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark,
            IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
        at System.Reflection.RuntimeAssembly.InternalLoadFrom(String assemblyFile, Evidence securityEvidence, Byte[] hashValue,
            AssemblyHashAlgorithm hashAlgorithm, Boolean forIntrospection,
                Boolean suppressSecurityChecks, StackCrawlMark& stackMark)
        at System.Reflection.Assembly.LoadFrom(String assemblyFile)
        at clrModule.PyInit_clr()

    In that case, I suggest to get the source at
    `sdpython/pythonnet <https://github.com/sdpython/pythonnet>`_
    and to compile them with VS 2015 on your machine.
    It will import the missing DLL which I'm still trying to find out.
    The DLL was compiled on an Azure Virtual Machine.
"""

import sys
import platform
import os
import json
import clr


def vocal_synthesis(text, lang="fr-FR", voice="", filename=None):
    """
    Utilise la synthèse vocale de Windows

    @param      text        text à lire
    @param      lang        langue
    @param      voice       nom de la voix (vide si voix par défaut)
    @param      filename    nom de fichier pour sauver le résultat au format wav (vide sinon)

    .. exref::
        :title: Utiliser une DLL implémentée en C#
        :tag: Technique

        .. index:: C#,DLL

        Le code de la DLL est le suivant. Il a été compilé sous forme de DLL.

        ::

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

        Pour l'utiliser, il faut utiliser l'instruction :

        ::

            from ensae_teaching_cs.pythonnet import clr
            from clr import AddReference
            AddReference("ENSAE.Voice")

        Si le programme répond qu'il ne trouve pas le fichier, il suffit
        d'inclure de la répertoire où se trouve la DLL dans la liste ``sys.path``.
        Ensuite on écrit simplement :

        ::

            from ENSAE.Voice import Speech
            Speech.VocalSynthesis(text, lang, voice, filename)

        Il faut voir le notebook :ref:`pythoncsharprst`.
    """
    if "ENSAE.Voice" not in sys.modules:
        if not sys.platform.startswith("win"):
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path, "csdll")

        from clr import AddReference

        try:
            AddReference("ENSAE.Voice")
        except Exception:
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path, "csdll")
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
    if "MagicJupyter" not in sys.modules:
        if not sys.platform.startswith("win"):
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path, "csdll")

        from clr import AddReference
        AddReference("System.Collections")

        try:
            AddReference("MagicJupyter")
        except Exception:
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path, "csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("MagicJupyter")

    from MagicJupyter import MagicCS
    return MagicCS


def str2python(answer):
    """
    Converts JSON bytes into a dictionary.

    @param      answer      bytes
    @return                 any type
    """
    json_obj = json.loads(answer)
    return json_obj


def vocal_recognition(subkey, lang="fr-FR", filename=None, memwav=None,
                      url="https://speech.platform.bing.com/recognize"):
    """
    Uses Cognitive Services to recognize the voice.

    @param      subkey      subscription key
    @param      lang        language
    @param      filename    wav file
    @param      memwav      wav memory stream
    @param      url         url of the service
    @return                 dictionary wih the results

    Either filename or memwav must be specified.
    """
    if filename is None and memwav is None:
        raise ValueError("Either filename or memwav must be filled.")
    if "ENSAE.Voice" not in sys.modules:
        if not sys.platform.startswith("win"):
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path, "csdll")

        from clr import AddReference

        try:
            AddReference("ENSAE.Voice")
        except Exception:
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path, "csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("ENSAE.Voice")

    from ENSAE.Voice import SpeechReco
    if filename is not None:
        res = SpeechReco.RunReco(subkey, filename, lang, url)
    else:
        res = SpeechReco.RunReco(subkey, memwav, lang, url)

    return str2python(res)


def vocal_recognition_listening(lang="fr-FR"):
    """
    Uses the recognition system and return sentances.

    @param      lang        language
    @return                 enumerate on tuples (score, text)
    """
    if "ENSAE.Voice" not in sys.modules:
        if not sys.platform.startswith("win"):
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path, "csdll")

        from clr import AddReference

        try:
            AddReference("ENSAE.Voice")
        except Exception:
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path, "csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("ENSAE.Voice")

    from ENSAE.Voice import SpeechRecoSystem
    for item in SpeechRecoSystem.EnumerateRecognize(lang):
        yield item.Item1, item.Item2


def vocal_recognition_system(wav, lang="fr-FR"):
    """
    Uses the recognition system and return sentances.

    @param      wav         bytes or string for a filename
    @param      lang        language
    @return                 tuples (score, text)
    """
    if not isinstance(wav, (bytes, str)):
        raise TypeError("wav should be bytes or str.")
    if "ENSAE.Voice" not in sys.modules:
        if not sys.platform.startswith("win"):
            raise NotImplementedError("only available on Windows")

        path = os.path.abspath(os.path.split(__file__)[0])
        path = os.path.join(path, "csdll")

        from clr import AddReference

        try:
            AddReference("ENSAE.Voice")
        except Exception:
            path = os.path.abspath(os.path.split(__file__)[0])
            path = os.path.join(path, "csdll")
            if path not in sys.path:
                sys.path.append(path)
            AddReference("ENSAE.Voice")

    from ENSAE.Voice import SpeechRecoSystem
    item = SpeechRecoSystem.Recognize(wav, lang)
    if item is None or len(item) == 0:
        return None
    else:
        return [(it.Item1, it.Item2) for it in item]
