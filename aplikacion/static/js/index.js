let navbar = document.querySelector(".navbar");
window.onscroll = () => {
  let heightWindow = window.pageYOffset;
  console.log(heightWindow);
  if (heightWindow < 200) {
    navbar.style.backgroundColor = "blue";
  } else if (heightWindow >= 201 && heightWindow < 500) {
    navbar.style.backgroundColor = "pink";
  } else {
    navbar.style.backgroundColor = "green";
  }
};
