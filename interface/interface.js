<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <style media="screen">
      div{
        display:none;
      }
    </style>
    <script type="text/javascript">
      //making function to show specific page and hide the other 2
    function showPage(page){
        document.querySelectorAll("div").forEach(div =>{  //select all elements in() and loop throught them
          div.style.display ='none';   //set thier style to none.
        })// short hand to select all elements  in ()
      document.querySelector(`#${page}`).style.display ='block';
    }

    //making the buttons work

    //loading the page first then listen to all user's actions
    document.addEventListener('DOMContentLoaded', () =>{
      //selecting all button in the page and loop throught them
      document.querySelectorAll('button').forEach(button =>{
        //listent to the button clicked then do the following
        button.onclick = function(){
          //run the show page functino with the argument, take this button and access it's dataset property
          //and this data set which called page  "هاتولي الكلب ده"
          showPage(this.dataset.page)
          }
    })
  })
    </script>
    <meta charset="utf-8">
    <title>Single page</title>
  </head>
  <body>
    <!--Making buttons to display the div sections on click of eacg-->
    <button data-page ="page1">Page 1</button>
    <button data-page ="page2">Page 2</button>
    <button data-page ="page3">Page 3</button>

    <!--making 3 div to manipulate with our js code-->
    <div id ="page1">
      <h1>this is page 1</h1>
    </div>
    <div id ="page2">
      <h1>this is page 2</h1>
    </div>
    <div id ="page3">
      <h1>this is page 3</h1>
    </div>
  </body>
</html>
///////////////
// when i press back in the browser go back to the last part of the page I have been on
    window.onpopstate = function(event){ //when I pop something from the history, take event as argument
      console.log(event.state.section);// what state that was requested from the user history
      showSection(event.state.section);// run our showSection() function to show it to the world , whoooo
    }
//the window object is so powerful it represnts the window my user sees,
//for example
window.innerWidth  //how wide is the window , good to know the size of users screen
window.innerHeight //how tall is the window , good to know the size of users screen
window.scrollY      //how many pixels far down have you scrolled, (in the Y axis)
document.body.offsetHeight   //what is the height of our document
//window is the physical screen that the user sees
//use to manipulate the contet to fit users window
//using all of those function we can do an interesting calcualtions ,
//for example how to know that the user reached the bottom of the page ?
if (window.innerHeight + window.scrollY  == document.body.offsetHeight)

parseInt(string) //convert a string to an integer

//reactive is another way of programming , not  imperative programming
///////////now it's time for react and imperative programming//////
//react will allow us to design user interactive web pages
