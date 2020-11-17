import json
import os
import base64
import pdfkit

PDF_PATH = '/tmp/out.pdf'

lambda_task_root_env = os.environ.get("LAMBDA_TASK_ROOT")
lambda_task_root = "" if not lambda_task_root_env else lambda_task_root_env
os.environ["PATH"] = os.environ["PATH"] + ":" + lambda_task_root + "/bin"

def format_response(response) -> dict:
    '''Formata a resposta HTTP'''
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf",
            "Access-Control-Allow-Origin" : "*"
        },
        "body": response,
        "isBase64Encoded": True
    }

def convert(page: str) -> str:
    '''Converte a página para PDF'''
    pdfkit.from_url(page, PDF_PATH)
    data = open(PDF_PATH).read()
    return base64.b64encode(data)

def get(event, context) -> dict:
    '''Trabalha a requisição para converter e responder com HTTP'''
    if event["queryStringParameters"]["reportUrl"]
        page: str = event["queryStringParameters"]["reportUrl"]
    else
        page: str = ""

    converted: str = convert(page)
    return format(converted)
