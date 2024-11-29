from hang_game import play_game

def main():
    while True:
        play_game()
        replay = input("\nХотите сыграть снова? (да/нет): ").strip().lower()
        if replay not in ["да", "д", "yes", "y"]:
            print("Спасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()
