"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This file uses the class BreakoutGraphics to build a game similar to breakout clone. When the user clicks the mouse,
the ball will fall, and the user could scroll the mouse to move the paddle, in order to rebound the ball to hit the
bricks. The game ends when either all bricks have been removed, or the number of lives has been depleted.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        vx = graphics.get_x_speed()
        vy = graphics.get_y_speed()
        graphics.ball.move(vx, vy)

        # Check if the ball hits the paddle or any bricks
        graphics.hit_ball_or_brick()
        # Rebound when hit the boundary of the window, except for the lower one
        if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
            graphics.set_x_speed(-vx)
        if graphics.ball.y < 0:
            graphics.set_y_speed(-vy)
        # When the ball falls under the lower boundary, the number of lives will minus 1 and the ball will reset
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.restart()
            num_lives -= 1
        pause(FRAME_RATE)

        # Ends the game
        if num_lives == 0:
            game_over = GLabel('Game Over.')
            game_over.font = '-40'
            graphics.window.add(game_over, graphics.window.width / 2 - game_over.width / 2,
                                graphics.window.height / 2 + game_over.height)
            break
        if graphics.brick_number == 0:
            win = GLabel('You Win!')
            win.font = '-40'
            graphics.window.add(win, (graphics.window.width - win.width) / 2, (graphics.window.height + win.height) / 2)
            graphics.window.remove(graphics.paddle)
            graphics.window.remove(graphics.ball)
            break


if __name__ == '__main__':
    main()
