while True:
    website= input ("enter website:  "  )

    if website.startswith("http://"):
        print ("Thank you for giving a valid link")
        break
    else:
        print("invalid link")