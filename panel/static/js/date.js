function startTime() {
    var today = new Date();
    var time = setTimeout(startTime, 500);
    var hr = today.getHours();
    var min = today.getMinutes();
    var sec = today.getSeconds();
    var months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    var days = ['Dom', 'Lun', 'Mar', 'Miér', 'Juev', 'Vier', 'Sáb'];
    var curWeekDay = days[today.getDay()];
    var curDay = today.getDate();
    var curMonth = months[today.getMonth()];
    var curYear = today.getFullYear();
    var date = curWeekDay + ", " + curDay + " " + curMonth + " " + curYear;
    var ap = (hr < 12) ? "<span>AM</span>" : "<span>PM</span>";
    hr = (hr == 0) ? 12 : hr;
    hr = (hr > 12) ? hr - 12 : hr;
    hr = checkTime(hr);
    min = checkTime(min);
    sec = checkTime(sec);
    document.getElementById("clock").innerHTML = date + " | " + hr + ":" + min + ":" + sec + " " + ap;
 }
 
 function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
 }
 
 // Llama a startTime() cuando la página se haya cargado completamente
 window.addEventListener('load', startTime);

 