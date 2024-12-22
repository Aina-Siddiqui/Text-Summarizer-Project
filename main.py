from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME='Data Ingestion_stage'
try:
    logger.info(f">>>>>Starting stage {STAGE_NAME}>>>>>")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>Completed stage {STAGE_NAME}<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    