def check_password(fawn_byte):
    return int('0b1100100011100000011100100110001', 2).to_bytes(
        (int('0b1100100011100000011100100110001', 2).bit_length() + 7) // 8,
        'big').decode() == fawn_byte

