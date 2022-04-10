#!/usr/bin/env python


from brain_games.engine import launch_game
from brain_games.games import game_gcd


def main():
    launch_game(game_gcd)


if __name__ == '__main__':
    main()
