# Sahil Patel

def encode(password):
    encoded_password = ""
    list_password = list(password)
    for i in range(len(list_password)):
        list_password[i] = int(list_password[i]) + 3
        if list_password[i] >= 10:
            list_password[i] = list_password[i] - 10
        encoded_password = encoded_password + str(list_password[i])
    return encoded_password


def decode(encoded_password):
    decoded_password = ''
    for i in encoded_password:
        x = int(i) - 3
        if x < 0:
            x += 10
        decoded_password += str(x)
    return decoded_password


if __name__ == '__main__':

    quit = False
    while not quit:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        if option == 2:
            decoded_password = decode(encoded_password)
            print("The encoded password is", encoded_password, "and the original password is", decoded_password + ".\n")

        if option == 3:
            quit = True