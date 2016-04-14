from users.models import User


def email_to_username(user_data):

    # from IPython import embed; embed()

    if "@" in user_data:
        is_have_email = User.objects.filter(
                email=user_data
        ).exists()

        if is_have_email:
            user = User.objects.get(
                    email=user_data,
            )
            return user.username
        return user_data
    return user_data
