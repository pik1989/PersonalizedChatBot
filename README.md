# PersonalizedChatBot

Build a Chatbot using Python/Flask

Chatbots are being made to ease the pain that the industries are facing today. The purpose of chat bots is to support and scale business teams in their relations with customers. It could live in any major chat applications like Facebook Messenger, Slack, Telegram, Text Messages, etc. 

This article shows how to create a simple chatbot in Python & Flask using the ChatterBot library. Our bot will be used for small talk, as well as to answer some math questions. Here, we’ll scratch the surface of what’s possible in building custom chatbots and NLP in general. 

<!-- wp:heading {"level":3} -->
<h3>Installing dependencies</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install chatterbot
pip install chatterbot_corpus</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3>Importing Classes - Getting started!!</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3>Creating the bot</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We are creating a Flask app, to get started with Flask, you can visit  <a href="https://www.flaskapi.org/"><strong><em>Here</em></strong></a> </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>app = Flask(__name__)
#bot = ChatBot("Pikachu")</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>We can create and train the bot by creating an instance of ListTrainer and supplying it with the lists of strings: </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>trainer = ListTrainer(bot)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Getting started with the training part, there are different ways how we can train the bot, by this,</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>trainer.train(['What is your name?', 'My name is Pikachu'])
trainer.train(['How are you?', 'I am good' ])
trainer.train(['Bye?', 'Bye, see you later' ])</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>or, we can also train by this,</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>conversation = [
    "Hello",
    "Hello!!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer.train(conversation)</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":3} -->
<h3>Training the Bot with corpus of data</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You can use your own or an existing corpus of data to train a bot. For example, you can use some corpus provided by chatterbot (inbuilt features): </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>The&nbsp;<strong>run()</strong>&nbsp;method of Flask class runs the application on the local development server. </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Yay, our first model is ready, let's test our bot.<br>The above given&nbsp;<strong>Python</strong>&nbsp;script is executed from Python shell. </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>python app.py</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>A message in Python shell informs you that </p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</code></pre>
<!-- /wp:code -->
