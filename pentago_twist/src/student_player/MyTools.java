package student_player;

import boardgame.Move;
import pentago_twist.PentagoBoardState;
import pentago_twist.PentagoCoord;
import pentago_twist.PentagoMove;

public class MyTools {
    public Move playCenter(PentagoBoardState boardState, int playerId){
      
        // for the first rounds, place piece in the centers
        PentagoCoord c1 = new PentagoCoord(1, 1);
        PentagoCoord c2 = new PentagoCoord(4, 1);
        PentagoCoord c3 = new PentagoCoord(1, 4);
        PentagoCoord c4 = new PentagoCoord(4, 4);
        Move myMove = boardState.getRandomMove();
    
        if(boardState.isPlaceLegal(c1)){
          myMove = new PentagoMove(c1, 1, 0, playerId);
        }
        else if(boardState.isPlaceLegal(c2)){
          myMove = new PentagoMove(c2, 1, 0, playerId);
        }
        else if(boardState.isPlaceLegal(c3)){
          myMove = new PentagoMove(c3, 1, 0, playerId);
        }
        else if(boardState.isPlaceLegal(c4)){
          myMove = new PentagoMove(c4, 1, 0, playerId);
        }
        return myMove;
      }
}