// const poems = document.querySelectorAll(".poem-text")
// const showButtons = document.querySelectorAll('.show-button')

// function hidePoem(poem) {
//   console.log(poem)
//   if (poem.hidden) {
//     setTimeout(() => {poem.hidden = false}, 0)
//   } else {
//     setTimeout(() => {poem.hidden = true}, 0)
//   }
// } 
// let counter = 0
// for(button in showButtons) {
//   let poem = poems[counter]
//   button.addEventListener('click', hidePoem(poem))
// }

function hidePoem(name) {
  let poemdiv = document.getElementsByName(name)
  poemdiv = poemdiv[0]
  console.log(poemdiv)
  if (poemdiv.hidden) {
    poemdiv.hidden = false
  } else {
    poemdiv.hidden = true
  }
}