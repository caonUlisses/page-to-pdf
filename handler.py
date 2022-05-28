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
    text = open(PDF_PATH, 'rb').read()
    return base64.b64encode(text).decode('utf-8')

def get(event, _) -> dict:
    '''Trabalha a requisição para converter e responder com HTTP'''
    if event["queryStringParameters"] and event["queryStringParameters"]["reportUrl"]:
        page: str = event["queryStringParameters"]["reportUrl"]
    else:
        page: str = "www.google.com"

    converted: str = convert(page)
    return format_response(converted)

