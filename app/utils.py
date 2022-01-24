from passlib.context import CryptContext


pw_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hashFunction(password : str):
    return pw_context.hash(password)

