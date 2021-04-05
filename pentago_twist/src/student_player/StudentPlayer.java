package student_player;

import boardgame.Move;
import pentago_twist.PentagoPlayer;
import pentago_twist.PentagoBoardState;

/** A player file submitted by a student. */
public class StudentPlayer extends PentagoPlayer {

    /**
     * You must modify this constructor to return your student number. This is
     * important, because this is what the code that runs the competition uses to
     * associate you with your agent. The constructor should do nothing else.
     */
    public StudentPlayer() {
        super("260681550");
    }

    /**
     * This is the primary method that you need to implement. The ``boardState``
     * object contains the current state of the game, which your agent must use to
     * make decisions.
     */
    public Move chooseMove(PentagoBoardState boardState) {
        Minimax minimax = new Minimax();
        MyTools myTools = new MyTools();
        PentagoBoardState pbs = (PentagoBoardState) boardState.clone();
        Move myMove;
        int turn_nb = pbs.getTurnNumber();
        System.out.println(turn_nb);
        if(turn_nb < 3) {
            myMove = myTools.playCenter(boardState, this.player_id);
        }
        else {
            
            myMove = minimax.alphaBetaPruning(boardState);
        }

        // Return your move to be processed by the server.
        return myMove;
    }
}