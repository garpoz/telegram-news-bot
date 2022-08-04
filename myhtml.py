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
    <body style="background-color:#002b5b">
        <div class="row" id="ck">
            <img id="img-id" class="nam row" src="./input.png" alt="Error Load Image">
            <img class="row s-i" id="chap" src="./chap.png" alt="Error Load Image">
            <img class="row s-i" id="rast" src="./rast.png" alt="Error Load Image">
            <div id="all-text"><span  class="bottom">{self.up_text}<br></span ><span class="text">{self.text}</span><br><span class="cap">{self.cap}</span></div>
        </div>
    </body>
</html>
"""
        return text
