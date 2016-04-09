from hashids import Hashids


def make_hash(instance):

    hashid = Hashids(
            min_length=10,
            salt=instance._meta.model_name,
    )

    return hashid.encode(instance.id)
