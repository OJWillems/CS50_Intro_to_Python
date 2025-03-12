import re
import sys

def main():
    html_input = input("HTML: ")
    print(parse(html_input))

def parse(html_string):
    pattern = r"<iframe.*youtube\.com/embed/(?P<video_id>\w+)[^\w].*</iframe>"
    if matches := re.search(pattern, html_string):
        video_id = matches.group("video_id")
        return f"https://youtu.be/{video_id}"

if __name__ == "__main__":
    main()