import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def TAPRA2026(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


@app.route(route="receber", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def receber(req: func.HttpRequest) -> func.HttpResponse:

    parametro = req.params.get("parametro")

    if not parametro:
        return func.HttpResponse("Nenhum parametro foi informado.", status_code=400)

    return func.HttpResponse(f"Parametro recebido: {parametro} | Resposta da Azure Function HTTP", status_code=200)


@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def timer_http(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("The timer is past due!")

    url = "http://localhost:7071/api/receber?parametro=chamada-do-timer"

    resposta = requests.get(url)

    logging.info("Resposta da função HTTP:")
    logging.info(resposta.text)

    logging.info("Python timer trigger function executed.")