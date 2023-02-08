from voluptuous import Schema


create_single_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    }
)

register_single_user = Schema(
    {
        "id": int,
        "token": str
    }

)

update_single_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    }
)

login_single_user_successful = Schema(
    {
        "token": str
    }
)

login_single_user_unsuccessful = Schema(
    {
        "error": str
    }
)