export FLASK_RUN_PORT=80
export FLASK_RUN_HOST="0.0.0.0"
export CON_CSV="./Assignment_Docs/concentration.timeseries.csv"

flask --app ConcentrationController run