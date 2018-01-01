from flask import render_template
from . import main


#使用蓝图添加到下面的路由404错误
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# 使用蓝图添加到下面的路由500错误
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

