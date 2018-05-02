"""
@file
@brief sound helpers
"""
import os
import sys


def convert_music_file(infile, outfile, format="wav", ffmpeg="ffmpeg.exe"):
    """
    Converts a music file using `pydub <https://pypi.python.org/pypi/pydub>`_
    and `ffmeg <http://www.ffmpeg.org/>`_.
    It converts a music file into another format.

    @param      infile      file to convert
    @param      outfile     file to produce
    @param      format      format (mp3, wav, ...)
    @return                 outfile
    """
    from pydub import AudioSegment

    if not os.path.exists(ffmpeg):
        raise FileNotFoundError(ffmpeg)

    if sys.platform.startswith("win"):
        AudioSegment.ffmpeg = ffmpeg
        path = os.path.dirname(ffmpeg)
        if path not in os.environ["PATH"]:
            os.environ["PATH"] = path + ";" + os.environ["PATH"]

    sound = AudioSegment.from_mp3(infile)
    sound.export(outfile, format=format)
    return outfile
