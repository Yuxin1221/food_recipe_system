from pywebio.input import *
from pywebio.output import *
from pywebio import session
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio import start_server



# `task_func` is PyWebIO task function


#input("This is a simple text input")
#input("hello word")
#select("This is a drop down menu", ['Option1', 'Option2'])
#checkbox("Multiple Choices!", options=["a",'b','c','d'])
#radio("Select any one", options=['1', '2', '3'])
#textarea('Text Area', rows=3, placeholder='Multiple line text input')
aaa = ""
def task_func():
    put_markdown('**Food recommendation system**').style('color: black; font-size: 50px; text-align: center' );
    put_text("Given a list of ingredients, get what your need! ?🍳").style('color: black; font-size: 20px' );
    put_markdown('For example, say I want to use up some food in my apartment, what can I cook? 🏠 My ML based model will look through over 4500 recipes to find matches for you... 🔍 Try it out for yourself below!')
    put_image('https://d18mqtxkrsjgmh.cloudfront.net/public/2021-03/Eating%20More%20Ultraprocessed%20‘Junk’%20Food%20Linked%20to%20Higher%20CVD%20Risk.jpeg').style('display: block;margin-left: auto;margin-right: auto;')


    aaa=input('PLease input our ingredient!', type=TEXT, placeholder='This is your ingredient', required=True)


    print(aaa)
    return aaa



def startServer():
    app = Flask(__name__)
    app.add_url_rule('/tool', 'webio_view', webio_view(task_func),
                methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    start_server(task_func,auto_open_webbrowser=True)
    app.run(host='localhost', port=80)
    return aaa


# 输出可以点击的按钮
#def on_click(btn):
    #put_markdown("You click `%s` button" % btn)

#put_buttons(['Give me recommedation!'], onclick=on_click);

