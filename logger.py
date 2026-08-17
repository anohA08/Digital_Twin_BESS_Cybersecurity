import logging

logging.basicConfig(

    filename="results/simulation.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

logger = logging.getLogger(__name__)