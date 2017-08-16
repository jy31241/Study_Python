name = 'id';
value = 'Park';

var todayDate = new Date();
tadayDate.setHours(todayDate.getDate() + 7);
document.cookie = name = "=" = escape(value) + ";path=/;expires=" + todayDate.toGMTString() +"";
alert(document.cookie)