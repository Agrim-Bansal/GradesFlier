const urlbase = 'https://gradesflier.herokuapp.com/api/solve'

const req = {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
}

async function ask () {
  let useText = document.getElementById('text-or-img').checked

  let urlext = ''

  if (useText) {
    // Use Text
    let text = document.getElementById('text_question').value

    if (text.length == 0)
      return alert('You need to ask a question to get answers!')

    req.body = JSON.stringify({ text })
    urlext = '/text'
  } else {
    // Use Image
    let img = document.getElementById('img')

    urlext = '/image'
  }

  let res = await fetch(`${urlbase}${urlext}`, req)

  let data = await res.json()

  console.log(data)
  alert(data.pod[1].subpod.plaintext)
}
