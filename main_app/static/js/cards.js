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