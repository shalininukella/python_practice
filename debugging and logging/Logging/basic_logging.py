import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something went wrong!")


#output

# INFO:root:Application started
# WARNING:root:Low disk space
# ERROR:root:Something went wrong!
