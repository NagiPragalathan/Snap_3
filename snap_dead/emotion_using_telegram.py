import cv2
import telebot
import os
import requests
from deepface import DeepFace
from gtts import gTTS

# Set the camera resolution and image quality
width, height = 640, 480
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# Initialize the Telegram bot
bot_token = '5968646843:AAHEppRcf4dKuNxcSMTHhyZFAIAC2nPZ2lU'
bot = telebot.TeleBot(bot_token)

# Define a command handler for /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Welcome to the Emotion Detection Bot! Send me a photo and I will tell you the emotion.")

# Define a message handler for photos
@bot.message_handler(content_types=['photo'])
def photo_message(message):
    # Download the photo from Telegram
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    url = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'
    img_data = requests.get(url).content
    
    # Save the photo to a file
    with open('photo.jpg', 'wb') as f:
        f.write(img_data)
    
    # Analyze the emotions in the photo
    frame = cv2.imread('photo.jpg')
    result = DeepFace.analyze(frame, actions=['emotion'])
    emotions = result[0].get('emotion')
    
    # Convert the emotion to a spoken response using text-to-speech
    response = f'The emotion is {emotions}.'
    tts = gTTS(text=response, lang='en')
    tts.save('response.mp3')
    
    # Send the response voice message to the user
    with open('response.mp3', 'rb') as f:
        bot.send_voice(message.chat.id, f)
    
    # Delete the temporary files
    os.remove('photo.jpg')
    os.remove('response.mp3')

# Start the Telegram bot
bot.polling()
