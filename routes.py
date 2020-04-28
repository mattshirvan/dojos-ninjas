from config import app
from controller_functions import index, add

app.add_url_rule("/", view_func = index)
app.add_url_rule("/add", view_func = add, methods=['POST'])