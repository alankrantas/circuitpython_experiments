import board, digitalio, audioio, audiocore, audiomixer, time

# the pin has to support DAC
# on some boards it's DAC0/DAC1
audio = audioio.AudioOut(board.A0)

# you can have as many as channels (voice counts)!
mixer = audiomixer.Mixer(voice_count=1, # 1 voice (voices can play asynchronously)
                         channel_count=1, # 1 = mono
                         sample_rate=22050,
                         bits_per_sample=16,
                         samples_signed=True)

# use the mixer
audio.play(mixer)

# load a WAV file: has to be mono, 16 bit with sample rate 22,050 Hz
# the music are downloaded here:
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out
music = audiocore.WaveFile(open('StreetChicken.wav', 'rb'))

# play a file on a voice
mixer.voice[0].play(music)

# wait until finish
while mixer.voice[0].playing:
    pass
