function setCounterText(distMilliseconds) {
  let days = Math.floor(distMilliseconds / (1000 * 60 * 60 * 24));
  let hours = Math.floor(distMilliseconds % (1000 * 60 * 60 * 24) / (1000 * 60 * 60));
  let minutes = Math.floor(distMilliseconds % (1000 * 60 * 60) / (1000 * 60));
  let seconds = Math.floor(distMilliseconds % (1000 * 60) / 1000);
  text = `${days}d ${hours}h ${minutes}m ${seconds}s`
  $(".counter").text(text);
};

function startCountdown(finalDateTime) {
  setInterval(function () {
    let nowDateTime = new Date().getTime();
    let dist = finalDateTime - nowDateTime;
    setCounterText(dist);
  }, 500);
};


$(document).ready(function () {
  startCountdown(1613568745 * 1000)
});
