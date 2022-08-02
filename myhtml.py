#! /usr/bin/python
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-


class Index:
    def __init__(self, up_text: str = "", text: str = "", cap: str = "") -> None:
        self.up_text = up_text
        self.text = text
        self.cap = cap

    def insert_text(self) -> str:
        text = f"""
<!DOCTYPE html>
<html dir="rtl" lang="en">
    <head>
        <meta charset="UTF-8">
        <title>entekhab</title>
        <link rel="stylesheet" href="./style.css">
    </head>
    <body>
        <div class="row" id="ck">
            <img id="img-id" class="nam row" src="./input.png" alt="Error Load Image">
            <img class="row s-i" id="chap" src="./chap.png" alt="Error Load Image">
            <img class="row s-i" id="rast" src="./rast.png" alt="Error Load Image">
            <div class="bottom"><h4>{self.up_text}</h4></div>
            <div class="text"><h2>{self.text}</h2></div>
            <div class="cap"><h6>{self.cap}</h6></div>
        </div>
    </body>
</html>
"""
        return text
