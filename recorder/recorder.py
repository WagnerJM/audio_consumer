from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment 
import logging

# Create a custom logger
name = __name__
logger = logging.getLogger(name)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(f'/media/festplatte/public/logs/{name}.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

class AudioRecorder:

    """
    AudioRecorder:

    Opens Spotify track with Selenium, plays the opend track and records the sound.
    After recording saves to .wav file

    """

    def __init__(self,track):
        
        self.track = track

    def prepare_browser(self, settings):
        """
        creates a selenium webbrowser session with a specific profile and headless option
        returns created webdriver

        """
        logger.info("Browser options")
        options = Options()
        logger.info("Setting Browser headless")
        options.headless = True
        profile = webdriver.FirefoxProfile(settings['profile_path'])
        logger.debug("profile found")
        driver = webdriver.Firefox(
            options=options, 
            firefox_profile=profile,
            executable_path=settings['driver_path']
            )
        logger.info("Browser created")
        return driver

    def run(self, driver, track):
        logger.info("Creating track")
        track_id = track['id']
        url = f"https://open.spotify.com/track/{track_id}"
        fs = track['settings']['framesize']
        seconds = int(track['duration_ms'] / 1000)


        driver.get(url)
        logger.info("URL started")
            
        driver.find_element_by_css_selector("button.btn.btn-green").click()
            
        logger.info("recording")
        driver.find_element_by_css_selector("button.btn.btn-green").click()
        recording = sd.rec(int(fs * seconds), samplerate=fs, channels=2, blocking=True)
        driver.find_element_by_css_selector("button.btn.btn-green").click()

        logger.info("done")
        driver.quit()
        logger.info("saving file")
            
        try:
            write(f"/media/festplatte/public/recordings/input/{track['trackname']}.wav", fs, recording)
            logger.info("File saved")
            wave_file = AudioSegment.from_wav(f"/media/festplatte/public/recordings/input/{track['trackname']}.wave")
            wave_file.export(f"/media/festplatte/public/recordings/output/{track['trackname']}.mp3", format="mp3")
            return True
        except Exception as e:
            logger.error("File could not be created")
            logger.error(e)
                

