# GPT 3.5 bot for Telegram

#Introduction
I wrote this bot because it was inconvenient for me to open GPT in my phone.
Things that I liked about this program: 
1) Works fast unlike third-party telegram bots 
2) full functionality of GPT 3.5 
3) Records logs

#Description
The following libraries are used in the work of this bot:
1) python-telegram-bot
2) openai
3) logging

For the OpenAI library to work, it is required that it works in your country, otherwise use a VPN or proxy.

Bot commands: 
1)/start 
When sending the /start command, a welcome message is sent to the user, a dialog history is created, and the behavior of GPT is set as a "useful assistant".
2)message with text
when sending a text message, the program tries to find the history of a particular user's conversation with ChatGPT.
If one is found, the user's request is added to it and a response from ChatGPT is created.
If the story was not found, then a new story is created, a user request is added to it and a response from ChatGPT is created.
After creating a response, it is sent to the user and logs are recorded.

#Resources
1) python-telegram-bot - https://github.com/python-telegram-bot/python-telegram-bot
2) openai - https://github.com/openai/openai-python
3) logging - https://docs.python.org/3/library/logging.html

#Getting help
If the resources mentioned above do not answer your questions, write me an email at ilya-vor-github@mail.ru