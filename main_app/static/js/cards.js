function hidePoem(name) {
  let poemdiv = document.getElementById(name)
  let poembtn = document.getElementById(`${name}-btn`)
  // poemdiv = poemdiv[0]
  console.log(poemdiv)
  if (poemdiv.hidden) {
    poemdiv.hidden = false
    poembtn.innerHTML = `<i class="fas fa-times"></i>`
  } else {
    poemdiv.hidden = true
    poembtn.innerHTML = `<i class="fas fa-ellipsis-h"></i>`
  }
}


function hideNav() {
  let hiddenNav = document.querySelector(".hidden-nav")
  if (hiddenNav.hidden) {
    hiddenNav.hidden = false
  } else {
    hiddenNav.hidden = true
  }
}

let hamburger = document.querySelector(".hamburger")

hamburger.addEventListener("click", hideNav)