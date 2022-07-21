# TL;DR
4Chan information extraction engine with a [Streamlit](http://streamlit.io)
interface.


## Deploy
To deploy the *streamlit app* with **Docker**:
```
docker run -d \
           --name omegalurk \
           -v omegalurk_models:/models \
           -p 8501:8484 \
           ghcr.io/ragingtiger/omegalurk:master
```
Then simply open your browser to `http://localhost:8484` and you
should see the *streamlit* interface.

## Testing
Run the *automated tests* locally as follows:
```
cd OmegaLurk
bash tests/run_tests.sh
```

## FAQ
+ How to change *time zone*?
  - The default time zone is *America/New_York*, but this can be changed
    by simply setting the `TZ` environment variable on `docker run` as
    follows:
    ```
    docker run -d \
               --name omegalurk \
               -v omegalurk_models:/models \
               -p 8501:8484 \
               -e TZ='Asia/Bangkok'
               ghcr.io/ragingtiger/omegalurk:master
    ```
    This will set the *time zone* inside the container to *Asia/Bangkok*. For
    a list of available time zones plese see
    [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
+ Where are the HuggingFace models downloaded to?
  - The models are downloaded (*cached*) in the `/models transformers`
    directory, which the docker command in the [deploy](#deploy) section
    manages with *Docker volumes*.

+ Why is my model taking so long to execute?
  - When models are run for the first time, you can expect it will take some
    time to download from the
    [Model Hub](https://huggingface.co/docs/hub/models-the-hub). You can
    always monitor the *Docker logs* to see the progress of the *model
    downloads*, simply run `docker logs -f omegalurk` to see them.
