"""
@file
@brief Data for competitions
"""
from pyquickhelper.filehelper.encryption import encrypt_stream, decrypt_stream


def encrypt_data(password, input, output):
    """
    encrypt a file

    @param      input       input filename
    @param      output      output filename
    @param      password    The encryption key - a string that must be either 16, 24 or 32
                            bytes long. Longer keys are more secure. If the data to encrypt
                            is in bytes, the key must be given in bytes too.
    """
    if not isinstance(password, bytes):
        password = bytes(password, "ascii")
    encrypt_stream(password, input, output)


def decrypt_data(password, input, output):
    """
    decrypt a file

    @param      input       input filename
    @param      output      output filename
    @param      password    The encryption key - a string that must be either 16, 24 or 32
                            bytes long. Longer keys are more secure. If the data to encrypt
                            is in bytes, the key must be given in bytes too.
    """
    if not isinstance(password, bytes):
        password = bytes(password, "ascii")
    decrypt_stream(password, input, output)
