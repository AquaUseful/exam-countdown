let DAY_STR = " дн"
let HOUR_STR = " ч"
let MINUTE_STR = " мин"
let SECOND_STR = " с"

function setCounterText(distMilliseconds) {
  let days = Math.floor(distMilliseconds / (1000 * 60 * 60 * 24));
  let hours = Math.floor(distMilliseconds % (1000 * 60 * 60 * 24) / (1000 * 60 * 60));
  let minutes = Math.floor(distMilliseconds % (1000 * 60 * 60) / (1000 * 60));
  let seconds = Math.floor(distMilliseconds % (1000 * 60) / 1000);
  $(".counter-days").text(`${days}${DAY_STR}`);
  $(".counter-hours").text(`${hours}${HOUR_STR}`);
  $(".counter-minutes").text(`${minutes}${MINUTE_STR}`);
  $(".counter-seconds").text(`${seconds}${SECOND_STR}`);
};

function startCountdown(finalDateTime) {
  setInterval(function () {
    let nowDateTime = new Date().getTime();
    let dist = finalDateTime - nowDateTime;
    setCounterText(dist);
  }, 500);
};

function getTimestamp() {
  let ajaxParams = {
    method: "GET",
    dataType: "json"
  }
  let jqxhr = $.ajax("/api/timestamp", ajaxParams);
  jqxhr.done(function (data) {
    millis = data.timestamp * 1000;
    startCountdown(millis);
  });
};

$(document).ready(function () {
  getTimestamp();
});
