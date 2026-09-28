import pytest
from task6 import decode_vigenere_cipher

pytestmark = pytest.mark.bonus


def test_decode_basic_word():
    assert decode_vigenere_cipher("Rijvs, Uyvjn!", "key") == "Hello, World!"


def test_decode_key_shorter_than_text_wraps_around():
    assert decode_vigenere_cipher("Hflmo", "ab") == "Hello"
