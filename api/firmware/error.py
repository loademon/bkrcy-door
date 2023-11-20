from app import app, jsonify


class Error(Exception):
    """Base class for exceptions"""

    def __init__(self, msg: str) -> None:
        self.message = msg


@app.errorhandler(Error)
async def handle_error(error: Error):
    response = jsonify({"error": error.message})
    response.status_code = 404
    return response
