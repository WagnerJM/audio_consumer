from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sounddevice as sd
from scipy.io.wavfile import write

class AudioRecorder:

    def __init__(self, track):
        self.prepare_browser(track['settings'])

    def prepare_browser(self, settings):
        print("Browser options")
        options = Options()
        print("Setting Browser headless")
        options.headless = True
        profile = webdriver.FirefoxProfile(settings['profile_path'])
        print("profile found")
        driver = webdriver.Firefox(
            options=options, 
            firefox_profile=profile,
            executable_path=settings['driver_path']
            )
        print("Browser created")
        return driver

        def create(self, driver, track):
            print("Creating track")
            track_id = track['id']
            url = f"https://open.spotify.com/track/{track_id}"
            fs = track['settings']['framesize']
            seconds = int(track['duration_ms'] / 1000)


            driver.get(url)
            print("URL started")
            
            driver.find_element_by_css_selector("button.btn.btn-green").click()
            
            print("recording")
            driver.find_element_by_css_selector("button.btn.btn-green").click()
            recording = sd.rec(int(fs * seconds), samplerate=fs, channels=2, blocking=True)
            driver.find_element_by_css_selector("button.btn.btn-green").click()

            print("done")
            driver.quit()
            print("saving file")
            write(f"/media/festplatte/public/recordings/input/{track['trackname']}.wav", fs, recording)
            print("File saved")
            return True

