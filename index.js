var mainText = document.getElementById("mainText");
var submitButton = document.getElementById("submitButton");

function submitClick(){
  window.alert("Test test test ");
  var firebaseRef = firebase.databse().ref();

  firebaseRef.child("text").set("value");
}
