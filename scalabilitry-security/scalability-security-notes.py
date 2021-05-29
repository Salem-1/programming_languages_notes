cashe-control: max-age=86400  # max number of seconds to store the case
#unless those number of seconds has elapsed we are going to use the existing version
#save the content in the browser cashed :)
#natural to have the css file cashed  in th ebrowser itself
ETag: "786464316xxxxxxx66"
#identify particular version of a resource ex:"css, html file"

# django has entire cash framework for the server side
# you have the privilage to store low level cahs API.template, per-view cahse

"""
-pay attentoin not to leak credentionals in Git :), if you did delete that old commit
-seek how to store credintials in the virtual machine to protect them
-pay attention to phishing attacks <a href="url1">url2</a>, if hoverover link it will show you where it's directing you
-pay attention to phishing attacks <a href="samestolenpage.com">url2</a>, copied site
-before sending data to routers we should encrypt them "cryptography"
    ->secret key cryptography , like cesar.py (encrypt and decrypt by key), not great approach
    -> Public-Key cryptography, here we use public key and private key... this is how the https works
    ->
-SQL threats
        ->sql injections "--
        ->use hashed version of password instead
        ->the forget password can leak information, through "there is no user with that email" message ,Opaaa
        ->data leak can be through measring time needed to get response that may represent  the number of quiries done, number of requests needed for that users
-APIs
    ->Rate limiting "restricting number of requesst DOS:denial of request , by many request that shut down the srever"
    ->Route authentication : "Permission models to access certain part of the data,"using API Key
    ->Don't put the API key inside your source code web application, use environment variable instead , define as variable that enquire from your protected resource
-javascript
        ->Cross-site scripting :running your js script on someone else's site , that can manipulate user experience to get specific result , can be run in the url if the developer allow any path to be typed in the url itself
        ->risk of making api requests and manipulate the dom,  come on the sky is the limit for that
        ->you should check for java script injection
        ->in messaging you can text someone js code that run when he recieve or open the message
        ->Cross site request forgery ; MAK FAKE REQUEST , like transefering money from the bank account like
        <body>
            <a href="http://yourbank.com/transfer?to=ahmed&amt=28000">
                Click Here ya zboon!
            </a>

            or

            <img src="http://yourbank.com/transfer?to=ahmed&amt=28000">
            or
            <body onload="document.forms[0].submit()"> # when the page is loaded go ahead and submit the first form, the user don't need to click submit ************
            <form class="" action="http://yourbank.com/transfer?to=ahmed&amt=28000" method="post">
              <input type="hidden" name="to" value="me">
              <input type="hidden" name="amt" value="2800">
              <input type="submit" name="" value="Click Here!">
            </form>
            #in this case user must inspect the source code
        ->Any site that change money must use post not get requests
        </body>
        {% csrf_token %}# of django protect from those attacks , as it changes for every session
        ->
"""

"""
resources:
web apps:server side :express.js   #very popular to build web apps ruby on rails 
client side to build user interfaces:angular jsreactvue.js ....
Deploying website:Amazon web services github pages   #use for static pagesgoogle cloud herokumicrisoft azure
"""
