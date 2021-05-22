//java allows adding logic and DOM manipulation in the client side

//inside the html under the head section
<script>
//printing something to the console (like python terminal)
cosole.log(something)



//to format a string use
`string ${variable}`
alert("something to be shown as alert in the brower") ;//built in function

//making function that listen to an event
function dosomething(){
  alert("I listend to your click")
}; //then make a buttom to take that function  as variable

//making another function that increment counter upon click
let counter = 0;  //defining a variable

function count(){
  counter++;   incrementing counter by 1
  alert(counter); //showing alert in the top of the browser
}
</script>
<body>
<button onclick="dosomething()"> CLick ME</button>
<button onclick="count()"> count</button>

</body>

/////////////////////////////////////manipulation of DOM////////////
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
   <script>
      function greet(){
   document.querySelector('h2').innerHTML = "Sobhan Allah";///////pay greet attention to the case senistivity of the functions name because it's counter intituitive , at least for now
      }
      //you can add logic else if as well

    </script>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h2>Bism Ellah</h2>
    <button Onclick="greet()" >Click here</button> //upon click it will change the <h2>Bism Ellah</h2> to <h2>Sobhan Ellah</h2>

  </body>
</html>

///////////////////////
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
   <script>
     //the == equality
     // the === strict equality type and value
     //document.querySelector('h2') can be stored in variable
     //let is changing variable, const is constant variable
     function greet(){
       const heading  = document.querySelector('h2');
   if (heading.innerHTML === "Sobhan Allah"){
     heading.innerHTML = "Bism Allah";
   }
        else{
          heading.innerHTML = "Sobhan Allah"
        }
      }

    </script>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h2>Bism Ellah</h2>
    <button Onclick="greet()" >Click here</button>

  </body>
</html>
////////////////adding event listener to the page
<script>
document.addEventListener('the event I want to listen to',what functoin to run after that event listener);
//you can write a function right in to the second argument in the
documnet.addEventListener('DOMContentLoaded',function(){

});

// the DOMContentLoaded load the entire HTML page first before running the script

</script>

//linking to separate js file

<script src="filename.js">

   </script>

   //backup to addEventListener
   //the == equality
    // the === strict equality type and value
    //document.querySelector('h2') can be stored in variable
    //let is changing variable, const is constant variable
    let  counter = 0;
    function count(){
      counter++;
      const heading  = document.querySelector('h2');
         heading.innerHTML = counter;
      if ((counter-1) % 10 === 0){  //  % mod return the remainder
        alert(`counter is ${counter}`)
      }

     }
    //ading event listner
    document.addEventListener('DOMContentLoaded',function(){
document.querySelector('button').addEventListener('click',count);
    }) //option1

 document.addEventListener('DOMContentLoaded',function(){
      document.querySelector('button').onclick =count;
      //make the counter count automatically
      //this is for the countdown features in the website
      setInterval(count,1000)
    })//option 2
   //notice it's not count(), it's just count
   ;
//running the querySelector using identifiers
document.querySelector('.class')
document.querySelector('#id')
document.querySelector('tag')  //for example <h1>


//getting the value or output of form submission

let variable = document.querySelector('#id').value;


///qurty selector for a  form
dcument.querySelector('form').onsubmit= FUNCTION(){
const name = document.querySelector('#name').value;

},

/////////// BEFORE THE data- attribute
<script>
//playing with the style properites
//changint the coloring h1 color
document.addEventListener('DOMContentLoaded',function(){

   //cahnging color to red
  document.querySelector('#red').onclick = function(){
    document.querySelector('#hello').style.color ='red';
        }
  document.querySelector('#green').onclick = function(){
    document.querySelector('#hello').style.color ='green';
        }
  document.querySelector('#blue').onclick = function(){
    document.querySelector('#hello').style.color ='blue';
        }
     })
</script>

    <h1 id="hello"> coloring</h1>

    <button id="red">Red</button>
    <button id="blue">Blue</button>
    <button id="green">Green</button>
    <!--yalehweeeey , 2ew33a ykoon elly fbaly-->
  ////// after the data attribute

  <script>

  </script>

//playing with the style properites
//changint the coloring h1 color

//loading the document first with the event listener
document.addEventListener('DOMContentLoaded',function(){

       //return an array or buttons as Nodes, forEach loop througth buttons
      document.querySelectorAll('button').forEach(function(button){
        //upon clicking that button
        button.onclick= function(){
          //get me the #hello and change it's color to whatever the color in the dataset of that button is
          document.querySelector('#hello').style.color =button.dataset.color;
      }



  <h1 id="hello"> coloring</h1>

     <button data-color="red">Red</button>
     <button data-color="blue">Blue</button>
     <button data-color="green">Green</button>
///////////////
// we can use => instead of function , where:
// function() == ()=>
//function(argument) == argument=>


//another way to change colors by using drop down list
<script>
document.addEventListener('DOMContentLoaded',() =>{ //load the page then listent to the events that's going to happem
document.querySelector('select').onchange = function(){  //get me the select menue ,and when there is a change in the select menue run the following function
document.querySelector("#hi").style.color = this.value;//means from this select menye
}

})
</script>

<h1 id="hi">Bism Ellah</h1>
  <select>
      <option value="red">Red</option>
      <option value="green">Green</option>
      <option value="blue">Blue</option>
  </select>

//Examples of event we can listen to
onlcick
onmousehover
onkeydown
onkeyup
onload
onblur
....

////making to do list simple project
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>To do list</title>
    <script >
    //remember the seceon t in content sir

//alert("script is working");
    document.addEventListener('DOMContentLoaded', function(){

      //disabled the submit button to protect the user from themseleves not to submit an emty task
       document.querySelector('#submit').disabled = true;

       //enabling the submit button when the user type something down
       document.querySelector('#task').onkeyup = () =>{
         // if the value of the task is not empty
         if(document.querySelector('#task').value.length > 0 )
           {
             document.querySelector("#submit").disabled = false;
           }
         else{
         document.querySelector("#submit").disabled = true;
            }
       }
    //   alert("DOMContenLoaded")
       //when the form is submitted do the followoing

 document.querySelector('form').onsubmit = () =>{
   //alert("form selected");

    // don't forget the # with the id sir
  //storing the task inputted in a variable
  const task = document.querySelector("#task").value;
   //creating an element inside html #Wow!
   let li =document.createElement('li');
   //inserting the task inside li element created up
   li.innerHTML = task;
  //alert("trying to append")
   //appending the li item in the tasks ul
   document.querySelector("#tasks").append(li);
   document.querySelector('#task').value = '';
//  alert('mision accomplished')
   //stop the form from submitting after the task is appended
   document.querySelector('#submit').disabled = true;
   return false;
   alert("error in appending and returning false of submission")
 }
})
   </script>
  </head>
  <body>
    <h1>task</h1>
    <ul id='tasks'>
    </ul>
    <form>
      <input type="text" id="task" placeholder="New Task" >
      <input id="submit" type="submit" >
    </form>

  </body>
</html>


function(arg){
  return value;
}
//can be written as
arg => value;
///////////////here comes an amazing feature, the local storage
localStorage.getItem(key)
localStorage.setItem(key,value) ;

//js objects like dictionaries in python

object = {kye: 'value',
          key2: 'value2'}

//now let's  dive in the API most important topic using:
//JSON java script object notation
//AJAX or ajax = asynchronous java script
//allow  us to make additional information to use in our page
//make a request to webpage and return it's promise = data of the requested site that may not come immediatly by the way
fetch('url')
.then(convert.json())//or text , you can convert to the format you like
.then(data =>{}) do//dosomething with the data you got
.catch(error =>{            //catching the error if it happened and print it in the console
  console.log("Error: ",error);
});
//Alf mabrook ya a7mad ya akhoia........
//remember to read the API documentation of each used  API
//how to round decimals
.toFixed(#)//# the number of digits to be rounded
