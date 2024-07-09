def main():
    fname = input("File name : ")
    ext = fname.split(".",1)[1]
    
    print(ext)

    match ext:
        case "jpg" | "jpeg" :
            print("image/jpg")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "pdf":
            print("image/pdf")            
        case "txt":
            print("image/txt")
        case "zip":
            print("image/zip")
        case _:
            print("application/octet-stream")

main()