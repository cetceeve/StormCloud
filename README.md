# StormCloud
Are storms blowing the cloud away?

# Data

Google Cloud Services Incidents historical data (json)
https://status.cloud.google.com/incidents.json

Google Cloud Services Incidents json schema
https://status.cloud.google.com/incidents.schema.json

We use the following command to download google's health reports.
```
wget --recursive --domains status.cloud.google.com --no-parent --html-extension --convert-links --no-clobber https://status.cloud.google.com/
```
The individual incident reports are then in `./status.cloud.google.com/incidents/`.
