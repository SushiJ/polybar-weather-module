class WeatherApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            error = "Rate limit reached. Please wait a minute and try again"
        else:
            error = f"Http Status code was: {status_code}."

        super().__init__("Api Error Occurred: " + error)
