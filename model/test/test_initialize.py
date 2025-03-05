if __name__ == '__main__':
    from cosyvoice.cli.cosyvoice import CosyVoice2
    model_path = '/external_data/models/CosyVoice2-0.5B_RWKV_0.19B/'
    device = 'cuda:0'
    cosyvoice = CosyVoice2(model_path,device=device,fp16=True)
    
    from cosyvoice.utils.file_utils import load_wav
    import torchaudio
    prompt_audio_file = '/home/yueyulin/github/RWKVTTS/mine.wav'
    prompt_audio_file = '/home/yueyulin/github/RWKVTTS/another.wav'
    prompt_audio_file = '/home/yueyulin/github/RWKVTTS/zero_shot_prompt.wav'
    prompt_speech_16k = load_wav(prompt_audio_file, 16000)
    prompt_text = '今天天气挺不错的。'
    prompt_text = '我家里有三只狗。'
    prompt_text = '希望你以后做的比我还好呦。'
    cosyvoice.model.llm.dummy_forward()
    for i, j in enumerate(cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', prompt_text, prompt_speech_16k, stream=False)):
        torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)