from data_collector import fetch_data
from data_cleaner import clean_data
from report_generator import generate_report

import schedule
import time


def run_pipeline():
    print("Executando pipeline...")
    fetch_data()
    clean_data()
    generate_report()
    print("Pipeline concluído")


# agendamento
schedule.every(1).minutes.do(run_pipeline)
# pode trocar por:
# schedule.every().hour.do(run_pipeline)
# schedule.every().day.at("09:00").do(run_pipeline)

print("Scheduler iniciado...")

while True:
    schedule.run_pending()
    time.sleep(1)