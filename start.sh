export FLASK_RUN_PORT=80
export FLASK_RUN_HOST="127.0.0.1"
export CON_CSV="./Assignment_Docs/concentration.timeseries.csv"

flask --app ConcentrationController run