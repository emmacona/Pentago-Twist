package student_player;

import java.util.ArrayList;

import boardgame.Board;
import pentago_twist.PentagoBoardState;
import pentago_twist.PentagoMove;

public class Minimax {
  private int alpha = -Integer.MAX_VALUE; // At max nodes, update α only
  private int beta = Integer.MAX_VALUE; // At min nodes, update β only
  private int WIN = 10;
  private int DRAW = 5;
  private int LOSE = 0;

  private class Move {	
      private int value;
      private PentagoMove pentagoMove;
      
      public Move(int value) {
          this.value = value;
      }
 
      public int getValue() {
        return this.value;
      }
      
      public PentagoMove getPentagoMove() {
        return this.pentagoMove;
      }
      
      public void setPentagoMove(PentagoMove pentagoMove) {
        this.pentagoMove = pentagoMove;
      }
  }

   public PentagoMove alphaBetaPruning(PentagoBoardState boardState){
      boolean isMaximize = true;

      Move bestMove = minimaxDecision(boardState, 0, isMaximize, alpha, beta);

      return bestMove.getPentagoMove();
   }

   public Move minimaxDecision(PentagoBoardState boardState, int depth, boolean isMaximize, int alpha, int beta){
    ArrayList<PentagoMove> allMoves = boardState.getAllLegalMoves();
    PentagoBoardState clonedBoardState;
    Move move;

    if (depth == 5 || boardState.gameOver()) {
			int value = minimaxValue(boardState);
			return new Move(value);
		}

    if (isMaximize){
      Move bestMove = new Move(-Integer.MAX_VALUE);
      for (PentagoMove pentagoMove : allMoves) {    
        clonedBoardState = (PentagoBoardState) boardState.clone();
        clonedBoardState.processMove(pentagoMove);
        move = minimaxDecision(clonedBoardState, depth+1, false, alpha, beta);

        // Update bestMove
        if(bestMove.getValue() < move.getValue()){
          // new move is better
          bestMove = move;
          bestMove.setPentagoMove(pentagoMove);
        }

        // At max nodes, update α only
        if(move.getValue() > alpha){
          alpha = move.getValue(); // update to max(alpha, bestValue);
        }

          // Prune in the event of inconsistency (α ≥ β)
        if (beta <= alpha) break;
      }
      return bestMove;
    }
    else {
      Move bestMove = new Move(-Integer.MAX_VALUE);
      for (PentagoMove pentagoMove : allMoves) {    
        clonedBoardState = (PentagoBoardState) boardState.clone();
        clonedBoardState.processMove(pentagoMove);
        move = minimaxDecision(clonedBoardState, depth+1, false, alpha, beta);

        // Update bestMove
        if(bestMove.getValue() > move.getValue()){
          // new move is better
          bestMove = move;
          bestMove.setPentagoMove(pentagoMove);
        }

        // At max nodes, update β only
        if(move.getValue() < beta){
          beta = move.getValue(); // update to min(beta, bestValue);
        }

          // Prune in the event of inconsistency (α ≥ β)
        if (beta <= alpha) break;
      }
      return bestMove;
   }
  }

  public int minimaxValue(PentagoBoardState boardState){
    int player = boardState.getTurnPlayer();
    if (boardState.gameOver()) {
			if (boardState.getWinner() == player) {
				return WIN;
			}
			else if (boardState.getWinner() == Board.DRAW) {
				return DRAW;
			}
			else {
				return LOSE;
				}
		}
    return 0;
  }

}
