from ariadne import MutationType
from api.types import Error
import requests

mutation = MutationType()
@mutation.field("askBot")
def create_session_resolver(obj, info, input):
    try:
        res = requests.post(
            "http://127.0.0.1:3001/api/v1/ask",
            json={"message": input.get("message")},
            headers={"Content-Type": "application/json"},
        ).json()
        return res

    except Exception:
        return {
            "success": False,
            "error": Error(
                message="Something went wrong on the server", field="server"
            ).to_json(),
        }
