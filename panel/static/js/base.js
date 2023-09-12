const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");
const themeTogglerPersonal = document.querySelector(".theme-toggler-personal");

// show sidebar menu
menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
})

// close sidebar menu
closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
})

// chance theme toggle
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})

// chance theme toggle
themeTogglerPersonal.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeTogglerPersonal.querySelector('span:nth-child(1)').classList.toggle('active');
    themeTogglerPersonal.querySelector('span:nth-child(2)').classList.toggle('active');
})

$(function() {
    $(".toggle").on("click", function() {
        if ($(".item").hasClass("active")) {
            $(".item").removeClass("active");
            $(this).find("a").html("<i class='fas fa-bars'></i>");
        } else {
            $(".item").addClass("active");
            $(this).find("a").html("<i class='fas fa-times'></i>");
        }
    });
});

function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
