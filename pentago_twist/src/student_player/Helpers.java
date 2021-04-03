package student_player;

import pentago_twist.PentagoBoardState;
import pentago_twist.PentagoPlayer;

public class Helpers {

  public int getCurrentPlayer(PentagoBoardState boardState){
    return boardState.getTurnPlayer();
  }
  
}
