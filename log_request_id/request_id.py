import uuid
import os

DEFAULT_REQUEST_ID_OBJECT_NAME: str = os.getenv('DEFAULT_REQUEST_ID_OBJECT_NAME', default='request_id')



def setup_context_getters() -> list:
    DEFAULT_REQUEST_ID_OBJECT_NAME: str = os.getenv('DEFAULT_REQUEST_ID_OBJECT_NAME', default='request_id')
    ...
    return []


REQUEST_ID_CONTEXT_GETTERS = setup_context_getters()


def current_request_id():
    for request_id_context_getter in REQUEST_ID_CONTEXT_GETTERS:
        try:
            request_id = request_id_context_getter()
        except ImportError:
            # if framework not installed skip
            continue

        if request_id is not None:
            return request_id


def register_context_getter(getter):
    if getter not in REQUEST_ID_CONTEXT_GETTERS:
        REQUEST_ID_CONTEXT_GETTERS.append(getter)

    return getter


def default_request_id_generator():
    return str(uuid.uuid4())
