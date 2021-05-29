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
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependencies\n",
    "import numpy as np\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Setup database\n",
    "#create engine\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "\n",
    "#reflect database and tables\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#save table references\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "\n",
    "#create session\n",
    "session = Session(engine)\n",
    "\n",
    "#Setup Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a function that gets minimum, average, and maximum temperatures for a range of dates\n",
    "# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' \n",
    "# and return the minimum, average, and maximum temperatures for that range of dates\n",
    "def calc_temps(start_date, end_date):\n",
    "    \"\"\"TMIN, TAVG, and TMAX for a list of dates.\n",
    "    \n",
    "    Args:\n",
    "        start_date (string): A date string in the format %Y-%m-%d\n",
    "        end_date (string): A date string in the format %Y-%m-%d\n",
    "        \n",
    "    Returns:\n",
    "        TMIN, TAVE, and TMAX\n",
    "    \"\"\"\n",
    "    \n",
    "    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set Flask Routes\n",
    "\n",
    "@app.route(\"/\")\n",
    "def main():\n",
    "    \"\"\"Lists all available routes.\"\"\"\n",
    "    return (\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/<start><br/>\"\n",
    "        f\"/api/v1.0/<start>/<end>\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    \"\"\"Return a JSON representation of a dictionary where the date is the key and the value is \n",
    "    the precipitation value\"\"\"\n",
    "\n",
    "    print(\"Received precipitation api request.\")"
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
