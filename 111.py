import speech_recognition as sr
import time

# 设置唤醒词
WAKE_WORD = "小瑞小瑞"

# 初始化语音识别器
recognizer = sr.Recognizer()


def listen_for_wake_word(recognizer, wake_word):
    with sr.Microphone() as source:
        print("等待唤醒词...")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                said = recognizer.recognize_google(audio, language='zh-CN')
                print("你说了: " + said)
                if wake_word in said:
                    print("唤醒词检测到，准备开始或继续对话。")
                    return True
            except sr.WaitTimeoutError:
                print("没有声音输入，继续等待。")
            except sr.UnknownValueError:
                print("无法理解语音输入。")


def handle_conversation(recognizer, wake_word):
    while True:
        print("现在可以进行对话。")
        try:
            recognizer.adjust_for_ambient_noise(sr.Microphone())
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                response = recognizer.recognize_google(audio, language='zh-CN')
                print("你说了: " + response)
                # 这里可以添加对话逻辑
                # 例如，根据response来决定如何回复
                # 假设我们只是简单地重复用户的话
                print("Kimi: " + response)

                # 检查是否再次说出唤醒词，如果是，则重新开始对话
                if wake_word in response:
                    print("唤醒词再次检测到，中断当前对话，等待新的指令。")
                    break
        except sr.WaitTimeoutError:
            print("没有声音输入，等待新指令。")
        except sr.UnknownValueError:
            print("无法理解语音输入。")


def main():
    while True:
        if listen_for_wake_word(recognizer, WAKE_WORD):
            handle_conversation(recognizer, WAKE_WORD)


if __name__ == "__main__":
    main()