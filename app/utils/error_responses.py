"""Error responses for the API."""

from collections.abc import Collection

# Define constants for error descriptions
ERROR_DESCRIPTIONS = {
    422: "Validation Error",
}


def add_error_responses(
    status_codes: list[int],
) -> dict[int, dict[str, Collection[str]]]:
    """
    Generate error responses based on status codes.
    :param status_codes: List of status codes.
    :return: Dictionary of error responses.
    """

    error_responses = {
        code: {
            "description": description,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": f"#/components/schemas/{description.replace(' ', '')}"
                    }
                }
            },
        }
        for code, description in ERROR_DESCRIPTIONS.items()
        if code in status_codes
    }

    return error_responses
