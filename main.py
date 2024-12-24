from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
STAGE_NAME='Data Ingestion stage'
try:
    logger.info(f">>>>>Starting stage {STAGE_NAME}>>>>>")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>Completed stage {STAGE_NAME}<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Data Validation stage'
try:
    logger.info(f">>>>>Starting stage {STAGE_NAME}>>>>>")
    data_validation= DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>Completed stage {STAGE_NAME}<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e   


STAGE_NAME='Data Transformation  stage'
try:
    logger.info(f">>>>>Starting stage {STAGE_NAME}>>>>>")
    data_transformation= DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>Completed stage {STAGE_NAME}<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e   