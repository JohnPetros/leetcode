texts = """BCDEFGBWF
BCDEFGTQRS
GYHMUAYGUPY
GYHMUAYGMJKL
YJSMFR FYJSHFT FAJ
YJSMFR FYJSHFT XUVW
***
RTQIITCOCFQI, XQEG GUVC FQPXQECFQ RCTC C HKECN FC OCTCVQPC. CXG
JOJDJFN B QSPHSBNBDBP JNFEJBUBNFOUF.BWF
HJXFW IJYJWRNSF: SFT TZXJR JMWFW JXYJ UWTILWFRF! FAJ
P TFOBEP DPOQJSNB, SFBMJABS FTUB QSPHSBNBDBP UFN HSBOEF VSHFOEJB. TQRS
KPHQIQOG O EQPUWN IQOCPQ UQDTG UGW RTOIITGUUQ.URST
RES IWUYIGEQ HE UYIFVE HI PMRLE RS JMREP.WIUV
***""".splitlines()


def decrypt_char(c, k):
    if "A" <= c <= "Z":
        index = ord(c) - ord("A")
        new_index = (index - k + 26) % 26
        return chr(new_index + ord("A"))
    else:
        return c


for line in texts:
    if line == "***":
        break

    words = line.split()
    if not words:
        print()
        continue

    last_word = words[-1]
    last_char_target = ""

    if len(last_word) % 2 != 0:
        last_char_target = "E"
    else:
        last_char_target = "R"

    last_char_encoded = last_word[-1]

    index_encoded = ord(last_char_encoded) - ord("A")
    index_target = ord(last_char_target) - ord("A")

    key = (index_encoded - index_target + 26) % 26

    decrypted_chars = []
    for char in line:
        decrypted_chars.append(decrypt_char(char, key))

    decrypted_line = "".join(decrypted_chars)

    print(decrypted_line)
