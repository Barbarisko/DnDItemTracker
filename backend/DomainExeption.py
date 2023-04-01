
class DatabaseGatewayError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Error in DB communication" + super().__str__()