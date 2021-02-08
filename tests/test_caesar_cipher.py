import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_encrypt_shift_4():
    actual = encrypt('hello world', 4)
    expected = 'lipps asvph'
    assert actual == expected

def test_decrypt_shift_4():
    actual = decrypt('Lipps Asvph', 4)
    expected = 'Hello World'
    assert actual == expected

def test_encrypt_shift_4_upper_case():
    actual = encrypt('Hello World', 4)
    expected = 'Lipps Asvph'
    assert actual == expected

def test_encrypt_special_character_and_white_space():
    actual = encrypt('hello.     world!', 4)
    expected = 'lipps.     asvph!'
    assert actual == expected

def test_crack():
    code = encrypt('It was the best of times, it was the worst of times. ', 3)
    actual = crack(code)
    expected = 'It was the best of times, it was the worst of times. '
    assert actual == expected