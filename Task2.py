def check_password(s, n):
    if n < 4:
        return 0

    if s[0].isdigit():
        return 0

    has_digit = False
    has_upper = False

    for ch in s:
        if ch == ' ' or ch == '/':
            return 0
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    if has_digit and has_upper:
        return 1
    else:
        return 0

password = input("Enter Password:").strip()
print(check_password(password, len(password)))