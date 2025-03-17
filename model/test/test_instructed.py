import time


def do_tts(tts_text,prompt_audios,prompt_texts,cosyvoice,prefix):
    import logging
    for i in range(len(prompt_audios)):
        prompt_audio_file = prompt_audios[i]
        prompt_speech_16k = load_wav(prompt_audio_file, 16000)
        for j in range(len(prompt_texts)):
            prompt_text = prompt_texts[j]
            logging.info(f'Processing {prompt_text} from {prompt_audio_file}')
            torch.cuda.manual_seed_all(time.time())
            for result in cosyvoice.inference_instruct2(tts_text,prompt_text, prompt_speech_16k, stream=False,speed=1):
                torchaudio.save(f"{prefix}_{i}_{j}.wav", result['tts_speech'], cosyvoice.sample_rate)
            logging.info(f'Finished processing {prompt_text} from {prompt_audio_file}')
if __name__ == '__main__':
    from cosyvoice.cli.cosyvoice import CosyVoice2
    import torch
    import sys
    # model_path = '/home/yueyulin/models/CosyVoice2-0.5B_RWKV_0.19B/'
    # device = 'cuda:0'
    print(sys.argv)
    model_path = sys.argv[1]
    device = sys.argv[2] if len(sys.argv) > 2 else 'cuda:0'
    cosyvoice = CosyVoice2(model_path,device=device,fp16=False,load_jit=False)
    
    from cosyvoice.utils.file_utils import load_wav
    import torchaudio
    prompt_audios = [
        # '/home/yueyulin/github/RWKVTTS/zero_shot_prompt.wav',
        '/home/yueyulin/github/RWKVTTS/mine.wav',
        # '/home/yueyulin/github/RWKVTTS/new.wav',
        # '/home/yueyulin/github/RWKVTTS/Trump.wav',
    ]
    
    prompt_texts = [
            '尝试一下以机器人的角色和我交流。',
            '请用悲伤的语气说话。',
            '请用上海话说下一句话。'
        ]
    
    # do_tts('By unifying streaming and non-streaming synthesis within a single framework, CosyVoice 2 achieves human parity naturalness, minimal response latency, and virtually lossless synthesis quality in streaming mode. ',prompt_texts,cosyvoice,"instructed_en")
    
    do_tts('[laughter]有时候，看着小孩子们的天真行为[laughter]，我们总会会心一笑。',prompt_audios,prompt_texts,cosyvoice,"instructed_cn")