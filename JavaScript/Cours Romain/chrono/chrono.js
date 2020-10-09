
// var timerDiv = document.createElement('div');
// timerContainer.appendChild(timerDiv);
// displayTimer.appendChild(timerDiv);

/*
var timer = setInterval(function(){
    timeSec += 1;
}, 1000);
*/


var timerDisplay = document.getElementById('displayTimer');
var listDisplay = document.getElementById('displayList');
var startBtnDisplay = document.getElementById('start');

var milliTime = 0;
var secondTime = 0;
var minuteTime = 0;
var timer;

var pause = false;

var startTime = Date.now();
var pauseTime = Date.now();



function Start() {

    if (timer === undefined && pause == false)
    {
        startTime = Date.now();
        ChronoSet();
    }
    else
    {
        Stop();
        Start();
    }
}


function Pause()
{
    if (pause == false)
    {
        pauseTime = Date.now() - startTime;
        clearInterval(timer);
        pause = true;
    }
    else if (pause == true && timer != undefined)
    {
        startTime =  Date.now() - pauseTime;
        ChronoSet();
        pause = false;
    }
}


function Lap()
{
    var temps = (minuteTime + "").padStart(2, '0') + ":" + (secondTime + "").padStart(2, '0') + ":" + (milliTime + "").padStart(3, '0');

    var timerList = document.createElement('div');
    timerList.textContent = temps;
    listDisplay.appendChild(timerList);
}


function Stop()
{
   clearInterval(timer);
        timerDisplay.textContent = "00:00.000";
        milliTime = 0;
        secondTime = 0;
        minuteTime = 0;
        timer = undefined;
        pause = false;
        startBtnDisplay.textContent = "Start";
}


function ChronoSet ()
{
    timer = setInterval(function ()
    {
        var currentTime = Date.now() - startTime;
        milliTime = currentTime % 1000;
        secondTime = (Math.floor(currentTime / 1000)) % 60;
        minuteTime = (Math.floor(currentTime / 60000)) % 60;

        timerDisplay.textContent = (minuteTime + "").padStart(2, '0') + ":" + (secondTime + "").padStart(2, '0') + ":" + (milliTime + "").padStart(3, '0');
    }, 50);

    startBtnDisplay.textContent = "Restart";
}