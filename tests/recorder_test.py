from recorder.recorder import AudioRecorder
import pika

#TODO: Add sample data for test
data = {}

def test_connection_to_rabbitMQ():
    pass


def test_AudioRecorder():
    recorder = AudioRecorder(data)
    recorder_state = recorder.create()

    assert recorder_state == True
