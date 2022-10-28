import subprocess
import logging
import sys
from time import sleep
import uuid

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def ping_cache():
    cmd = "redis-cli ping"
    result = subprocess.run(cmd, shell = True,capture_output=True)
    res = result.stdout.decode("UTF-8")
    if res == "":
        logging.info(f"redis not running")
        return False
    if res != "":
        logging.info(f"redis running")
        return True

def bootstrap():
    if not ping_cache():
        cmd = "./start_cache.sh"
        result = subprocess.run(cmd, shell = True,capture_output=True)
        res = result.stdout.decode("UTF-8")
        print(res)


if __name__=="__main__":
    bootstrap()
