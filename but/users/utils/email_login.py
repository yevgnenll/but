from users.models import User


def email_to_username(user_data):

    # from IPython import embed; embed()

    if "@" in user_data:
        user = User.objects.get(
                email=user_data,
        ) or user_data
        return user.username
    else:
        return user_data
