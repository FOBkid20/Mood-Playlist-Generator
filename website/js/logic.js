const ANGER = 0;
const CONTEMPT = 1;
const DISGUST = 2;
const FEAR = 3;
const HAPPINESS = 4;
const SURPRISE = 5;
const NEUTRAL = 6;


const HAPPY_LIST = "https://open.spotify.com/embed/user/spotify/playlist/37i9dQZF1DXdPec7aLTmlC";
const SAD_LIST = "https://open.spotify.com/embed/user/spotify/playlist/37i9dQZF1DXaJZdVx8Fwkq";
const ANGRY_LIST = "https://open.spotify.com/embed/user/piiamaria-/playlist/1aUGVrGipiT9vOb11jO4n4";

function generatePlaylist(emotion){
  if(emotion == "anger")){
    emotion = ANGER;
  }else if(emotion == "contempt"){
    emotion = CONTEMPT;
  }else if(emotion  == "disgust"){
    emotion = DISGUST;
  }else if(emotion == "fear"){
    emotion = FEAR;
  }else if(emotion == "happiness") {
    emotion = HAPPINESS;
  }else if(emotion == "surprise"){
    emotion = SURPRISE;
  }else{
    emotion = NEUTRAL;
  }
  switch (emotion){
    case ANGER:
      document.getElementById("link").innerHTML = ANGRY_LIST;
      break;
    case CONTEMPT:
      document.getElementById("link").innerHTML = ANGRY_LIST;
      break;
    case DISGUST:
      document.getElementById("link").innerHTML = ANGRY_LIST;
      break;
    case FEAR:
      document.getElementById("link").innerHTML = SAD_LIST;
      break;
    case HAPPINESS:
      document.getElementById("link").innerHTML = HAPPY_LIST;
      break;
    case SURPRISE:
      document.getElementById("link").innerHTML = HAPPY_LIST;
      break;
    case NEUTRAL:
      document.getElementById("link").innerHTML = HAPPY_LIST;
      break;
  }
}
