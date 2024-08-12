from flask import Flask, request, render_template
from src.db_manager import get_db_manager
from src.utils import get_cst_time
from datetime import datetime

#Fecha, hora, ubicacion

app = Flask(__name__)
db_client = get_db_manager("condo-logs")


@app.route("/get_logs", methods=["GET"])
def get_logs():
	register_logs = list(db_client["registros-bitacora"].find())
	for register in register_logs:
		register["fecha"] = get_cst_time(register["fecha"])
	return render_template("index.html",documents=register_logs)


@app.route("/log",methods=["GET"])
def log():
	log_id = request.args.get("id")
	current_timestamp = datetime.timestamp(datetime.now())
	register_log = {
		"ubicacion": log_id,
		"fecha": current_timestamp
	}
	try:
		db_client["registros-bitacora"].insert_one(register_log)
	except Exception as e:
		print(e)

	if int(log_id) > 13:
		raise Exception("Ubicacion no valida")
	return f"<p>Registro de bitacora exitoso</p> <p>ID:{register_log['ubicacion']}</p><p>{get_cst_time(register_log['fecha'])}</p>"

@app.route("/")
def main_page():
	return "<p>Welcome</p>"
