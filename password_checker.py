from bloom_filter import BloomFilter


def check_password_uniqueness(bloom: BloomFilter, passwords: list) -> dict:
    results = {}
    for password in passwords:
        if not isinstance(password, str) or not password.strip():
            results[password] = "некоректний"
            continue

        if password in bloom:
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
            bloom.add(password)
    return results
