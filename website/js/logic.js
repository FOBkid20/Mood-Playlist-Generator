const ANGER = 0;
const CONTEMPT = 1;
const DISGUST = 2;
const FEAR = 3;
const HAPPINESS = 4;
const SURPRISE = 5;
const NEUTRAL = 6;


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
    case ANGER: break;
    case CONTEMPT: break;
    case DISGUST: break;
    case FEAR: break;
    case HAPPINESS: break;
    case SURPRISE: break;
    case NEUTRAL: break;
  }
}



document.getElementById("demo").innerHTML = x;
