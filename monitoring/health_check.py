import os

LOG_FILE = "logs/pipeline.log"


def pipeline_status():

    if os.path.exists(LOG_FILE):

        print("Pipeline Log Found")

    else:

        print("Pipeline Not Executed")
