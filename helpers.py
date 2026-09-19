import uuid


def generate_email():
    return f'desk{uuid.uuid4().hex[:10]}@mail.ru'


def generate_ad_title():
    return f'Книга {uuid.uuid4().hex[:8]}'
