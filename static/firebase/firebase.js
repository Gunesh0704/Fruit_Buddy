
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  apiKey: "AIzaSyBoJFZNJBYwPy14U2bfYDEjcLjLKDvXcZM",
  authDomain: "fruit-buddy-6e037.firebaseapp.com",
  projectId: "fruit-buddy-6e037",
  storageBucket: "fruit-buddy-6e037.appspot.com",
  messagingSenderId: "762245492241",
  appId: "1:762245492241:web:4509575fcdac5eb6d64bb0",
  measurementId: "G-TYNJ37L9F2",
  databaseURL: "https://fruit-buddy-6e037-default-rtdb.firebaseio.com",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
const auth = firebase.auth();

// Initialize Realtime Database and get a reference to the service
const database = firebase.database();



async function signup(e) {
  e.preventDefault()
  // const name = document.querySelector('#name')
  const email = document.querySelector('#email')
  // const ocuupation = document.querySelector('#occu')
  const password = document.querySelector('#password')

  try {

    const result = await firebase.auth().createUserWithEmailAndPassword(email.value, password.value)

    alert("Your Account is Sucessfully created !")
    console.log(result)
    window.location.href = "./index.html"
    firebase.auth().signOut()

  }
  catch (err) {
    console.log(err)
    alert("Please fill the form !")
  }


}



async function login(e) {
  e.preventDefault()
  const email = document.querySelector('#login-email')
  const password = document.querySelector('#login-pass')

  try {
    const result = await firebase.auth().signInWithEmailAndPassword(email.value, password.value)
    console.log(result)
    window.location.href = "./home.html"
    alert("You are sucessfully logged in !");
  }
  catch (err) {
    console.log(err)
    alert("Please enter Correct Email and Password !");
  }


}
firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    console.log(user)
  } else {
    console.log('signout success')
  }
});


async function loginWithGoogle() {
  try {
    var provider = new firebase.auth.GoogleAuthProvider();
    const result = await firebase.auth()
      .signInWithPopup(provider)
    console.log(result)
    window.location.href = "./home.html"
  }
  catch {
    console.log(err)
  }


}

function logout() {
  firebase.auth().signOut()
  alert("Logged out Sucessfully !")
  window.location.href = "./index.html"
}

function forgotpass(){
  const email = document.querySelector('#login-email')
  firebase.auth().sendPasswordResetEmail(email.value)
  .then(() => {
    // Password reset email sent!
    // ..
    alert("Password reset email sent!")
  })
  .catch((error) => {
    console.log(error)
  });
}