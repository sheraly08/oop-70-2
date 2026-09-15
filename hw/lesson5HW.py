from faker import Faker
# Эта библиотека нужна для генерации фальшивых, но реалистичных тестовых данных (имена, email, адреса)

fake = Faker()
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
