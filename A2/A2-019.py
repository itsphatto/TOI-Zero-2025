def analyze_bunny_message(message):
    msg = message.upper()
    max_u_count = 0
    found_buu = False

    for i in range(len(msg)):
        if msg[i] == 'B':
            j = i + 1
            u_count = 0
            while j < len(msg) and msg[j] == 'U':
                u_count += 1
                j += 1
            if u_count >= 2:
                found_buu = True
                max_u_count = max(max_u_count, u_count)

    if found_buu:
        print(f"Yes {max_u_count}")
    elif 'B' in msg or 'b' in message:
        index = next(i for i, c in enumerate(message) if c.lower() == 'b')
        print(message[:index+1] + 'U' * (len(message) - index - 1))
    else:
        repeated = ('BUU' * ((len(message) // 3) + 1))[:len(message)]
        print(repeated)

user_input = input()
analyze_bunny_message(user_input)
