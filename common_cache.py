
import bootstrap
import redis
import logging, sys, uuid, dill
from boltons import gcutils

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
r = redis.Redis(host='localhost', port=6379, db=0)
#bootstrap.bootstrap()

interpreter_id = f"intprid:{uuid.uuid4()}"
logging.info(f"This interpreter process's id is: {interpreter_id}")

__active_classes__ = set()




def write(obj: object) -> str:
    obj_id = f"{interpreter_id}::objtype:{type(obj).__name__}::objid:{uuid.uuid4()}"
    bytes_obj = dill.dumps(obj)
    r.set(obj_id, bytes_obj)
    logging.info(f"Wrote object to common cache with obj_id {obj_id}")
    return obj_id

def read(obj_id: str) -> object:
    obj_bytes = r.get(obj_id)
    if obj_bytes == None:    
        logging.error(f"No corrresponding object found in cache for key {obj_id}")
        return None
    else:
        obj = dill.loads(dill.loads(obj_bytes))
        __active_classes__.update(obj.__class__)
        return obj

def get_all(verbose: bool = False) -> list[object]:
    pipe = r.pipeline()
    keys = [key.decode("UTF-8") for key in r.keys()]
    if keys == []:
        logging.warn("No keys found in redis. No Objects Loaded")
        return None
    for key in keys:
        pipe.get(key)
    objs = [dill.loads(obj) for obj in pipe.execute()]
    if verbose: 
        for obj in objs: logging.info(f"Loaded {obj} from cache.")
    for obj in objs: __active_classes__.add(obj.__class__)
    return objs

def write_all(verbose: bool = False) -> bool:
    pipe = r.pipeline()
    for cls in __active_classes__:
        objs = gcutils.get_all(type_obj=cls, include_subtypes= False)
        for obj in objs:
            obj_id = f"{interpreter_id}::objtype:{type(obj).__name__}::objid:{uuid.uuid4()}"
            pipe.set(obj_id,dill.dumps(obj))
            if verbose: logging.info(f"Wrote {obj} to cache.")
    pipe.execute()

def flush_all() -> bool:
    r.flushall()