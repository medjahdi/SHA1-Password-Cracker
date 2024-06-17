import hashlib

def convert_txt_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    return digest


def main():
    user_sha1 = input("Enter The SHA1 to Crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    with open("./pass.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_txt_to_sha1(
                password)
            
            if cleaned_user_sha1 == converted_sha1:
                print(f"Password was FOUND! {password}")
                return
            
    print(f"Could NOT Find The Password! ")
            


            
if "__name__" == "__main__":
    main()

