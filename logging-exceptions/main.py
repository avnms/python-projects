import logging

logger = logging.getLogger(__file__)


class OutsideRangeException(Exception):
    pass


def range_check_user_input(value: int) -> float:
    if not 0 < value <= 100:
        raise OutsideRangeException("Range exceeded", value)
    return value


def get_data_from_user():
    successful = False
    while not successful:
        value = input(
            "Please enter an integer greater than 0 and less than or equal to 100: "
        )
        try:
            value = int(value)
        except ValueError as e:
            logger.exception("Something happened", e)
            print(e)
            continue

        try:
            result = range_check_user_input(value)
        except OutsideRangeException as e:
            logger.exception("Value outside of range", e)
            print(
                "Entered value outside of acceptable range, please re-enter a valid number"
            )
            continue
        print(f"Value within range = {result}")
        successful = True


if __name__ == "__main__":
    get_data_from_user()
