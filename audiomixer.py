import board, digitalio, audioio, audiocore, audiomixer, time

// the pin has to support DAC
audio = audioio.AudioOut(board.DAC0)

// you can have as many as channels (voice counts)!
// the WAV files has to be mono, 16 bit with sample rate 22,050 Hz
mixer = audiomixer.Mixer(voice_count=1, sample_rate=22050, channel_count=1,
                         bits_per_sample=16, samples_signed=True)

// the music are downloaded here:
// https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out
music = audiocore.WaveFile(open('StreetChicken.wav', 'rb'))

// use the audio mixer
audio.play(mixer)

// play music on a channel asynchronously
mixer.voice[0].play(music)

// wait until playing is finished
while mixer.voice[0].playing:
    pass
