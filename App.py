{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This python script uses flask and SQL alchemy to simulate API requests of weather data of Honolulu, HI."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependenices \n",
    "from flask import Flask, jsonify\n",
    "import numpy as np\n",
    "from sqlalchemy import create_engine\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import and_\n",
    "from sqlalchemy import or_\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy import func\n",
    "import datetime as dt\n",
    "from dateutil.relativedelta import relativedelta\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create engine\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an app\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "# home page\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    print(\"Server received request for 'Home' page...\")\n",
    "    return (\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br>\"\n",
    "        f\"/api/v1.0/stations<br>\"\n",
    "        f\"/api/v1.0/tobs<br>\"\n",
    "        f\"/api/v1.0/ + start date<br>\"\n",
    "        f\"/api/v1.0/ + start date/ + end date\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    print(\"Server received request for 'precipitation' page...\")\n",
    "    last_date = session.query(func.max(Measurement.date)).all()\n",
    "    last_date = last_date[0][0]\n",
    "    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d').date()\n",
    "    year_before_date = ((last_date - relativedelta(years = 1)).strftime('%Y-%m-%d'))\n",
    "    query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_before_date).order_by(Measurement.date.desc()).all()\n",
    "    data = {date: prcp for date, prcp in query}\n",
    "    return jsonify(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    print(\"Server received request for 'stations' page...\")\n",
    "    query = session.query(Station.station).all()\n",
    "    stations = list(np.ravel(query))\n",
    "    return jsonify(stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
