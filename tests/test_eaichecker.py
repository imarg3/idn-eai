import pytest

from eai import eaichecker


class TestEAIChecker:

    # 'mocker' fixture provided by pytest-mock
    @pytest.mark.parametrize("test_input, expected", [
        ("gmail.com", "TRUE"), ("gistmail.in", "TRUE"), ("जिस्टमेल.भारत", "TRUE"),
        ("डाटामेल.भारत", "TRUE")
    ])
    def test_check_smtputf8_support(self, mocker, test_input, expected):
        # Mock the slow function and return True always
        mocker.patch('eai.eaichecker.smtputf8_check', return_value='TRUE')
        assert eaichecker.smtputf8_check(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("yahoo.com", "FALSE"), ("cdac.in", "FALSE"), ("yahoo.co.in", "FALSE")
    ])
    def test_check_non_smtputf8_support(self, mocker, test_input, expected):
        # Mock the slow function and return True always
        mocker.patch('eai.eaichecker.smtputf8_check', return_value='FALSE')
        assert eaichecker.smtputf8_check(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("xyzt.cfsm", "EXCEPTION"), ("cdsaac.insd", "EXCEPTION"), ("yahoo.cofte.in", "EXCEPTION")
    ])
    def test_check_invalid_domain_smtputf8_support(self, mocker, test_input, expected):
        # Mock the slow function and return True always
        mocker.patch('eai.eaichecker.smtputf8_check', return_value='EXCEPTION')
        assert eaichecker.smtputf8_check(test_input) == expected
