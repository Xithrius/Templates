def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


from google.cloud import texttospeech as tts
client = tts.TextToSpeechClient()
response = client.list_voices

implicit()
