const $form = $('#form')
const $showTimer = $('#showTimer')
let $score = parseInt($('#score').text())
let seconds = 10

function timer() {
    setInterval(() => {
        if (seconds > 0) {
            seconds--
            $showTimer.text(`Time Remaining: ${seconds}`)
        }
        else {
            clearInterval()
            $form.remove()
        }
    }, 1000)
}

$form.submit(async function(e){
    e.preventDefault()
    const $guess = $('#guess').val()

    let res = await axios.post('/check-word', {'guess': $guess})
    const result = res.data.result
    checkWord(result)
})

const checkWord = (res) => {
    const $responseArea = $('#responseArea')
    const $guess = $('#guess').val()
    if (res === 'ok') {
        $responseArea.text('Word is Valid');
        $('#score').text($score += $guess.length);
    }
    if (res === 'not-on-board'){
        $responseArea.text('Word not on Board')
    }
    if (res === 'not-a-word'){
        $responseArea.text('Not a Valid Word')
    }
}

const sendStats = async () => {
    const finalScore = $score
    let data = await axios.post('/get-stats', {'score': finalScore})
}

timer()
sendStats()