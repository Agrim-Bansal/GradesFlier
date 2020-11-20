const urlbase = 'https://gradesflier.herokuapp.com/api/solve'

const req = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  }
}

async function ask() {
  document.getElementById('submit').disabled = true
  let useText = true // document.getElementById('text-or-img').checked

  let urlext = ''

  if (useText) {
    // Use Text
    let text = document.getElementById('text_question').value

    if (text.length == 0)
      return alert('You need to ask a question to get answers!')

    req.body = JSON.stringify({
      text
    })
    urlext = '/text'
  } else {
    // Use Image
    let img = document.getElementById('img')

    urlext = '/image'
  }

  let res = await fetch(`${urlbase}${urlext}`, req)

  let data = await res.json()

  let output = data.pod[1].subpod.plaintext
  var imgAnsEl = document.getElementById("img-answer")
  imgAnsEl.style.display = "none"
  if (output == null) {
    const imgAns = data.pod[1].subpod.img["@src"]
    if (imgAns != null) {
      imgAnsEl.style.display = "block"
      imgAnsEl.src = imgAns

    } else {
      output = "Answer not found."
      alert(output)
    }
  } else {
    alert(output)
  }
  document.getElementById('submit').disabled = false
}