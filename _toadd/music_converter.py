import os
import sys
import platform

from ..core.hal_log import HalLOG
from ..home.importme.importme import import_module


def convert_music_file(infile, outfile, format="wav"):
    """
    converts a music file using `pydub <https://pypi.python.org/pypi/pydub>`_
    and `ffmeg <http://www.ffmpeg.org/>`_.

    It converts a music file into another format.

    @param      infile      file to convert
    @param      outfile     file to produce
    @param      format      format (mp3, wav, ...)
    @return                 outfile
    """
    try:
        import pydub
    except ImportError:
        raise ImportError("pydub is missing, type pip install pydub")

    if sys.platform == 'win32':
        path = os.path.abspath(os.path.split(__file__)[0])
        ffmpeg = os.path.join(path, "ffmpeg.exe")
        if not os.path.exists(ffmpeg):
            ffmpeg = import_module("ffmpeg.zip", whereTo=path)[0]
            if not os.path.exists(ffmpeg):
                raise FileNotFoundError(
                    "unable to find ffmpeg.exe, copy it close to this file: " + os.path.abspath(__file__))
        from pydub import AudioSegment
        AudioSegment.ffmpeg = ffmpeg
        if path not in os.environ["PATH"]:
            os.environ["PATH"] = path + ";" + os.environ["PATH"]

    from pydub import AudioSegment
    sound = AudioSegment.from_mp3(infile)
    sound.export(outfile, format=format)
    return outfile


def translate_sound_file(culture, infile, print_console=False):
    """
    Translate speech into text using Windows speech recognition.
    It only works in Windows. (see `Get Started with Speech Recognition <http://msdn.microsoft.com/en-us/library/hh361683%28v=office.14%29.aspx>`_).

    See also `dragonfly <https://pypi.python.org/pypi/dragonfly/>`_.

    @param      culture         culture (fr-FR for example)
    @param      infile          file to convert
    @param      print_console   to print out some information about the process going on
    @return                     results (list of objects, see below)

    Example:
    @code
    file = "something.wav"
    res = translate_sound_file("fr-FR", file, __name__ == "__main__")
    for r in res :
        print(r.ToString())
        # or
        print(r.begin, r.duration, r.options[0].score, r.options[0].text)
    @endcode
    """

    if sys.platform == 'win32':
        path = os.path.abspath(os.path.split(__file__)[0])
        dll = os.path.join(path, "SoundToText.dll")
        if not os.path.exists(dll):
            dlls = import_module("SoundToText.zip", whereTo=path)
            if not os.path.exists(dll):
                raise FileNotFoundError(
                    "unable to find SoundToText.dll, copy it close to this file: " + os.path.abspath(__file__))

        if platform.architecture()[0] == "64bit":
            from .._externals.pythonnet64 import clr as CLR
        else:
            from .._externals.pythonnet import clr as CLR

        path, dll = os.path.split(dll)
        if path not in sys.path:
            sys.path.append(path)

        CLR.AddReference(dll.replace(".dll", ""))
        from SoundToText import SoundToTextASync

        obj = SoundToTextASync.Create(culture, infile, print_console)
        obj.RunRecognition()
        res = obj.Recognized
        return res
    else:
        raise Exception(
            "unable to recognize speech if not on Windows, look at module dragonfly")
