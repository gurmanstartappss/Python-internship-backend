class User:
    def __init__(
        self,
        name,
        email=None,
        age=None,
        phone=None,
        address=None,
        company=None,
        is_active=True
    ):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address
        self.company = company
        self.is_active = is_active


user = User(
    "abc",
    "sdfg@gmail.com",
    22,
    "1234567890",
    "indore",
    "ABC",
    True
)