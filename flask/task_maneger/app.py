import sqlite3
from flask import Flask, request, redirect, url_for, render_template, flash, session,g
#للتشفير
from werkzeug.security import generate_password_hash, check_password_hash
import functools
from blog import bp as blogbp
from auth import bp as authbp
app = Flask( __name__ )

#ياخذ الوسائط المفتاحية الممررة
app.config.from_mapping(SECRET_KEY="swewrnthmdnfxfzdxzsdrz@N#JWS<Xjudsdcm")


app.register_blueprint(blogbp)
app.register_blueprint(authbp)

app.add_url_rule('/',endpoint="blog.index")





app.run(debug=True)
#####
