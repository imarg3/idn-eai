import pytest
from eai.idn_services import IDNService


class TestIDNService:

    @pytest.fixture
    def idn(self):
        return IDNService()

    @pytest.mark.parametrize("idn_word, expected", [("मुद्रा", "मुद्गा,मुद्रा,मुद्ना"), ("किताब", "कित्ताब,किताब")])
    def test_generate_blocked_variants(self, idn, idn_word, expected):
        assert idn.generate_homograph_variants(idn_word) == expected

    def test_blocked_variants_return_type(self, idn):
        utf8_string = idn.generate_homograph_variants("मुद्रा")
        assert isinstance(utf8_string, str)

    @pytest.mark.parametrize("idn_word, expected", [("मुद्रा", "मुद्रा,मूद्रा"), ("किताब", "किताब,कीताब")])
    def test_generate_coallocatable_variants(self, idn, idn_word, expected):
        assert idn.generate_similar_phonic_variants(idn_word) == expected

    def test_blocked_coallocatable_return_type(self, idn):
        utf8_string = idn.generate_homograph_variants("मुद्रा")
        assert isinstance(utf8_string, str)
