# WhoDis?

WhoDis is a cloud-enabled, mobile-ready, application used for speech recognition for signing in across various social platforms.

  - Uses Google Speech API along with speech_recognition library in Python.
  - Goal : Add additional security to login portals across platforms.
  - Advantage : Unique passphrase generated at each login, enabling better security.

# Tech

  - All python source files (.py)
  - Twilio - 
        Used to receive text message on the linked phone number.
     -  https://www.twilio.com/
  - Google Speech API 
        To convert unique speech passphrase to text.
    -  https://cloud.google.com/speech-to-text/      
  - Chrome Extension for our application
    -   To connect social media platform of your choice for login features.


### Installation

WhoDis requires Python 3.7 to run.
Install the dependencies :

```sh
import speech_recognition as sr
import pyaudio
import wave
import random
from twilio.rest import Client
import time
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
   
   ### To-do
-   Decrease Authentication Time
    -   Authentication time disregarding network provider was around 2.5 seconds.
-   Chrome Extension
-   A more efficient mobile application   Time
    -   Application developed during the 48-hr event wasn't very efficient. 

   
  
