function run(){
	var black_list = ["pinche", "pendejo", "verga", "madre", "madres", "puta", "p***", "palta", "sombrilla"]
	var x = document.getElementById("audio");

	let rec;
		if (!("webkitSpeechRecognition" in window)) {
			alert("No ha sido posible concetar con la API");
		} else {
			rec = new webkitSpeechRecognition();
			rec.lang = "es-MX";
			rec.continuous = true;
			rec.interimResults = true;
			rec.addEventListener("result",iniciar);
		}
	function iniciar(event){
		var interim_transcript = '';
		var final_transcript = '';
		for (var i = event.resultIndex; i < event.results.length; ++i) {
			if (event.results[i].isFinal) {
				final_transcript += event.results[i][0].transcript;
			} else {
				interim_transcript += event.results[i][0].transcript;
			}
		}
		document.getElementById('texto').innerHTML = interim_transcript;
		isThisBad(interim_transcript);
	}

	function isThisBad(text){
		var b = false;
		var txt = text.split(" ");
		for (let i = 0; i < txt.length; i++){
			if (black_list.includes(txt[i])){
				b = true;
			}
		}
		if (b) {
			audio_play();
		}
	}

	function audio_play(){
		window.focus();
		x.play();
	}

	function errase_button(event){
		document.getElementById("b1").outerHTML = "";
	}

	rec.start();
}
