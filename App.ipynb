{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Flask\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "# Dependencies and Setup\n",
    "import numpy as np\n",
    "import datetime as dt\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from sqlalchemy.pool import StaticPool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Database Setup\n",
    "#Create engine\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reflect Database\n",
    "Base = automap_base()\n",
    "# Reflect the Tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save References to Each Table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Session (Link) From Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask Setup\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask Routes\n",
    "\n",
    "# Home Route\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    \"\"\"List all available api routes.\"\"\"\n",
    "    return (\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/2017-06-20<br/>\"\n",
    "        f\"/api/v1.0/2017-06-20/2017-06-28\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Precipitation Route\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "        # Calculate the Date 1 Year Ago from the Last Data Point in the Database\n",
    "        one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)\n",
    "        #Retrieve the Last 12 Months of Precipitation Data Selecting Only the date and prcp Values\n",
    "        precipitation_data = session.query(Measurement.date, Measurement.prcp).\\\n",
    "                filter(Measurement.date >= one_year_ago).\\\n",
    "                order_by(Measurement.date).all()\n",
    "        # Convert List of Tuples Into a Dictionary\n",
    "        precipitation_data_dic = dict(precipitation_data)\n",
    "        # Return JSON Representation of Dictionary\n",
    "        return jsonify(precipitation_data_dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Station Route\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "        # Return list of stations from the dataset\n",
    "        stations_data = session.query(Station.station, Station.name).all()\n",
    "        # Convert List of Tuples Into Normal List\n",
    "        station_list = list(stations_data)\n",
    "        # Return JSON List of Stations from the Dataset\n",
    "        return jsonify(station_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TOBs Route\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "        # Calculate the Date 1 Year Ago from the Last Data Point in the Database\n",
    "        one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)\n",
    "        # Retrieve the Last 12 Months of date and prcp Precipitation Data\n",
    "        tobs_data = session.query(Measurement.date, Measurement.tobs).\\\n",
    "                filter(Measurement.date >= one_year_ago).\\\n",
    "                order_by(Measurement.date).all()\n",
    "        # Convert List of Tuples Into List\n",
    "        tobs_list = list(tobs_data)\n",
    "        # Return JSON List of Temperature Observations (tobs) for the Previous Year\n",
    "        return jsonify(tobs_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Start Day Route\n",
    "@app.route(\"/api/v1.0/<start>\")\n",
    "def start_day(start):\n",
    "        start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "                filter(Measurement.date >= start).\\\n",
    "                group_by(Measurement.date).all()\n",
    "        # Convert List of Tuples Into Normal List\n",
    "        start_day_list = list(start_day)\n",
    "        # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start Range\n",
    "        return jsonify(start_day_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Start-End Day Route\n",
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def start_end_day(start, end):\n",
    "        start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "                filter(Measurement.date >= start).\\\n",
    "                filter(Measurement.date <= end).\\\n",
    "                group_by(Measurement.date).all()\n",
    "        # Convert List of Tuples Into Normal List\n",
    "        start_end_day_list = list(start_end_day)\n",
    "        # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start-End Range\n",
    "        return jsonify(start_end_day_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define Main Behavior\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
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
