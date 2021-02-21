// DOM elements
const guideList = document.querySelector(".guides");
<<<<<<< HEAD

=======
const go = document.querySelector(".go");
>>>>>>> 19e8c097ded31508329c9d43839c9a33e52c44d6
const loggedOutLinks = document.querySelectorAll(".logged-out");
const loggedInLinks = document.querySelectorAll(".logged-in");
const accountDetails = document.querySelector(".account-details");

const setupUI = (user) => {
  if (user) {
    db.collection("users")
      .doc(user.uid)
      .get()
      .then((doc) => {
        const html = `
          <div>Logged in as ${user.email}</div>
          <div>Name : ${doc.data().name}</div>
          <div>Bio : ${doc.data().bio}</div>
        `;
        accountDetails.innerHTML = html;
      });
    // toggle user UI elements
    loggedInLinks.forEach((item) => (item.style.display = "block"));
    loggedOutLinks.forEach((item) => (item.style.display = "none"));
<<<<<<< HEAD
    
=======
    go.style.display = "block";
>>>>>>> 19e8c097ded31508329c9d43839c9a33e52c44d6
  } else {
    // clear account info
    accountDetails.innerHTML = "";
    // toggle user elements
    loggedInLinks.forEach((item) => (item.style.display = "none"));
    loggedOutLinks.forEach((item) => (item.style.display = "block"));
<<<<<<< HEAD
   
=======
    go.style.display = "none";
>>>>>>> 19e8c097ded31508329c9d43839c9a33e52c44d6
  }
};

// setup guides
const setupGuides = (data) => {
  if (data.length) {
    let html = "";
    data.forEach((doc) => {
      const guide = doc.data();
      const li = `
            <li>
            <input style="opacity:1 ; pointer-events: auto; " type="radio" name="me" value='${guide.Time}' >
              <label style="font-size:30" class="grey lighten-4"> ${guide.Title} </label>
              <br>
              <label style="font-size:30" class="white"> ${guide.Time} </label>
            </li>
          `;
      html += li;
    });
    guideList.innerHTML = html;
  } else {
    guideList.innerHTML = '<h4 class="center-align">Login to view Todo</h4>';
  }
};

document.addEventListener("DOMContentLoaded", function () {
  var modals = document.querySelectorAll(".modal");
  M.Modal.init(modals);

  var items = document.querySelectorAll(".collapsible");
  M.Collapsible.init(items);
});
