register = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "savingAmount": {"type": "number"},
        "loanAmount": {"type": "number"}
    },
    "required": ["username", "password", "savingAmount", "loanAmount"]
}

access = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "password"]
}
