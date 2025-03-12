file_input = input("What file would you like to upload? ").strip().casefold()

def main(file):
    media_type = None

    # ### if / elif / else Method: ###

    # if file.endswith(".gif"):
    #     media_type = "image/gif"
    # elif file.endswith(".jpg") or file.endswith(".jpeg"):
    #     media_type = "image/jpeg"
    # elif file.endswith(".png"):
    #     media_type = "image/png"
    # elif file.endswith(".pdf"):
    #     media_type = "application/pdf"
    # elif file.endswith(".txt"):
    #     media_type = "text/plain"
    # elif file.endswith(".zip"):
    #     media_type = "application/zip"
    # else:
    #     media_type = "application/octet-stream"


    # ### Basic Match Method: ###

    # match file:
    #     case file if file.endswith(".gif"):
    #         media_type = "image/gif"
    #     case file if file.endswith(".jpg") | file.endswith(".jpeg"):
    #         media_type = "image/jpeg"
    #     case file if file.endswith(".png"):
    #         media_type = "image/png"
    #     case file if file.endswith(".pdf"):
    #         media_type = "application/pdf"
    #     case file if file.endswith(".txt"):
    #         media_type = "text/plain"
    #     case file if file.endswith(".zip"):
    #         media_type = "application/zip"
    #     case _:
    #         media_type = "application/octet-stream"


    # ### Advanced Match Method: ###

    match file.split(".")[-1]:
        case "gif":
            media_type = "image/gif"
        case "jpg" | "jpeg":
            media_type = "image/jpeg"
        case "png":
            media_type = "image/png"
        case "pdf":
            media_type = "application/pdf"
        case "txt":
            media_type = "text/plain"
        case "zip":
            media_type = "application/zip"
        case _:
            media_type = "application/octet-stream"

    print(media_type)
    return media_type

main(file_input)
