import handler
import pytest

def test_format_response():
    formated = handler.format_response("test")
    assert formated["statusCode"] == 200
    assert formated["headers"]["Content-Type"] == "application/pdf"
    assert formated["headers"]["Access-Control-Allow-Origin"] == "*"
    assert formated["body"] == "test"
    assert formated["isBase64Encoded"] == True

def test_convert():
    assert handler.convert != None

def get():
    params = {
        "queryStringParameters": {
            "reportUrl": "https://google.com"
        }
    }
    assert False != True
