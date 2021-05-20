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
