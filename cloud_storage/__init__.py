from google.cloud import storage

config_file_path = 'cloud_storage/gcs_storage_key.json'

# buckets
IMG_PROCESS_OUTPUT_BUCKET = 'img_process_output_bucket'
SEARCHEE_SAMPLE_BUCKET = 'searchee_sample_bucket'
FIR_BUCKET = 'fir_bucket'

client = storage.Client.from_service_account_json(config_file_path)