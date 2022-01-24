from passlib.context import CryptContext


pw_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hashFunction(password : str):
    return pw_context.hash(password)


def verify(plain_password,hashed_password):
    return pw_context.verify(plain_password,hashed_password)

