package student_player;

import java.util.ArrayList;

import boardgame.Board;
import boardgame.Move;
import pentago_twist.PentagoBoardState;
import pentago_twist.PentagoMove;
import pentago_twist.PentagoPlayer;

public class Minimax {
  private int alpha = -Integer.MAX_VALUE; // At max nodes, update α only
  private int beta = Integer.MAX_VALUE; // At min nodes, update β only
  private int WIN = 10;
  private int DRAW = 5;
  private int LOSE = -10;
  private MinmaxNode bestMove = new MinmaxNode(0);

  private class MinmaxNode {	
      private int value;
      private PentagoMove pentagoMove;
      
      public MinmaxNode(int value) {
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

   public Move alphaBetaPruning(PentagoBoardState boardState, long endTime){
      boolean isMaximize = true;
      bestMove = minimaxDecision(boardState, 0, isMaximize, alpha, beta, endTime);
      PentagoMove bestPentagoMove = bestMove.getPentagoMove();
      if(bestPentagoMove == null) {
        System.out.println("NOT FOUND - get random");
        return boardState.getRandomMove();
      } else {
        return bestMove.getPentagoMove();
      }  
   }

   public MinmaxNode minimaxDecision(PentagoBoardState boardState, int depth, boolean isMaximize, int alpha, int beta, long endTime){
    ArrayList<PentagoMove> allMoves = boardState.getAllLegalMoves();
    PentagoBoardState clonedBoardState;
    MinmaxNode move;

    while (System.currentTimeMillis() < endTime){
      if (depth == 2 || boardState.gameOver()) {
        int value = minimaxValue(boardState);
        return new MinmaxNode(value);
      }
  
      if (isMaximize){
        bestMove = new MinmaxNode(-Integer.MAX_VALUE);
        for (PentagoMove pentagoMove : allMoves) {    
          clonedBoardState = (PentagoBoardState) boardState.clone();
          clonedBoardState.processMove(pentagoMove);
          move = minimaxDecision(clonedBoardState, depth+1, false, alpha, beta, endTime);
  
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
        bestMove = new MinmaxNode(Integer.MAX_VALUE);
        for (PentagoMove pentagoMove : allMoves) {    
          clonedBoardState = (PentagoBoardState) boardState.clone();
          clonedBoardState.processMove(pentagoMove);
          move = minimaxDecision(clonedBoardState, depth+1, false, alpha, beta, endTime);
  
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
    System.out.println("TIMES UP");
    return bestMove; // if time's up, return bext move thus far
  }

  public int minimaxValue(PentagoBoardState boardState){
    int player = boardState.getTurnPlayer();
    int score = 0;
    // If the node is the end of a game, 
    if (boardState.gameOver()) {
			if (boardState.getWinner() == player) {
				score += WIN;
			}
			else if (boardState.getWinner() == Board.DRAW) {
				score += DRAW;
			}
			else {
				score += LOSE;
				}
		} 
    // The node does not represent the end of a game, but we can earn some points for particular paths
    else {
      score += bonusPoints(boardState, player);
    }
    return score;
  }

  public int bonusPoints(PentagoBoardState boardState, int player){
    int bonus = 0;
    int increment = 2;

    if (player == PentagoBoardState.WHITE){ // Note: this means student is playing first
      for (int i = 0; i <= 5; i++){
        // 1) diagonal
        String d1 = boardState.getPieceAt(i, i).toString();
        String d2 = boardState.getPieceAt((i+1)%6, (i+1)%6).toString(); // %6 to wrap around board limit
        if(d1.equals("w") && d2.equals("w")) bonus += increment; // bonus adjacent pieces along diagonal
        
        // 2) column
        String c1 = boardState.getPieceAt(i, i).toString();
        String c2 = boardState.getPieceAt(i, (i+1)%6).toString(); // %6 to wrap around board limit
        if(c1.equals("w") && c2.equals("w")) bonus += increment; // bonus adjacent pieces along diagonal

        // 3) row
        String r1 = boardState.getPieceAt(i, i).toString();
        String r2 = boardState.getPieceAt((i+1)%6, i).toString(); // %6 to wrap around board limit
        if(r1.equals("w") && r2.equals("w")) bonus += increment; // bonus adjacent pieces along diagonal

        increment += 2; // More pieces in a row == award more points
      }
    }
    else {
      for (int i = 0; i <= 5; i++){
        // 1) diagonal
        String d1 = boardState.getPieceAt(i, i).toString();
        String d2 = boardState.getPieceAt((i+1)%6, (i+1)%6).toString(); // %6 to wrap around board limit
        if(d1.equals("b") && d2.equals("b")) bonus += increment; // bonus adjacent pieces along diagonal
        
        // 2) column
        String c1 = boardState.getPieceAt(i, i).toString();
        String c2 = boardState.getPieceAt(i, (i+1)%6).toString(); // %6 to wrap around board limit
        if(c1.equals("b") && c2.equals("b")) bonus += increment; // bonus adjacent pieces along diagonal

        // 3) row
        String r1 = boardState.getPieceAt(i, i).toString();
        String r2 = boardState.getPieceAt((i+1)%6, i).toString(); // %6 to wrap around board limit
        if(r1.equals("b") && r2.equals("b")) bonus += increment; // bonus adjacent pieces along diagonal

        increment += 2; // More pieces in a row == award more points
      }
    }

    return bonus;
  }
}
